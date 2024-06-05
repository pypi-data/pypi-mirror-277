import glob
import json
import os
import uuid
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Optional

from peopledatalabs import PDLPY

from pdl_api.models.person import JsonPersonResponse, Person, PersonWrapper


@dataclass
class PDLPersonAPI:
    api_key: str
    storage_loc: Optional[str] = None
    existing_people: list[PersonWrapper] = field(default_factory=list)
    client: Optional[PDLPY] = None
    skip: set[str] = field(default_factory=set)

    def __post_init__(self):
        if not self.api_key:
            raise ValueError("api_key is required")
        if self.storage_loc:
            self.storage_loc = os.path.expanduser(self.storage_loc)
            os.makedirs(self.storage_loc, exist_ok=True)
            self.load_existing_people(self.storage_loc)
        if not self.client:
            self.client = PDLPY(api_key=self.api_key)

    def load_existing_people(self, storage_loc: str):
        """Load existing people from a directory of json files"""
        files = glob.glob(f"{storage_loc}/*.json")
        for file in files:
            with open(file, "r") as f:
                data = json.load(f)
                pw = PersonWrapper(**data)
                # pr = JsonPersonResponse(**data)
                # pw = PersonWrapper(
                #     person=Person(**pr.data),
                #     likelihood=pr.likelihood,
                #     dataset_version=pr.dataset_version,
                # )
                self.existing_people.append(pw)

    # def get_single_person(self, param: dict[str, Any]) -> Person:
    #     return None
    def person_enrichment(self, params: dict[str, Any]) -> list[Person]:
        """Get a person from the API"""
        if not self.client:
            raise ValueError("Client not initialized")
        json_response = self.client.person.enrichment(**params).json()
        response = JsonPersonResponse(**json_response)
        people = []
        if response.status == 200:
            data = response.data
            if isinstance(data, list):
                people = [Person(**d) for d in data]
            else:
                people = [Person(**data)]
        for p in people:
            if self.storage_loc:
                if not p.id:
                    p.id = str(uuid.uuid4())
                pw = PersonWrapper(
                    person=p,
                    likelihood=response.likelihood,
                    dataset_version=response.dataset_version,
                )
                with open(f"{self.storage_loc}/{pw.person.full_name}.json", "w") as f:
                    f.write(json.dumps(p.model_dump(mode="json")))
        return people

    def find_existing_person(self, params: dict[str, Any]) -> list[PersonWrapper]:
        """Find an existing person in the existing people"""
        people = []
        for pw in self.existing_people:
            match = True
            for key, value in params.items():
                ## TODO Currently only works with email and 1 email
                value = value[0]
                if key == "email":
                    for email in pw.person.emails or []:
                        if email.address in self.skip:
                            match = False
                            break
                        if email.address == value:
                            break
                    else:
                        match = False
                        break

            if match:
                people.append(pw)
        return people

    def get_person_via_email(self, email: str) -> list[PersonWrapper]:
        return self.get_person(params={"email": [email]})

    def get_person(
        self, params: dict[str, Any], skip_if_exists: bool = True
    ) -> list[PersonWrapper]:
        """Get a person from the API"""

        people = []
        ## convert to single params for API call
        ## ## TODO Right now works with 1 person..
        if skip_if_exists:
            existing = self.find_existing_person(params=params)
            ## remove existing people from params
            if existing:
                return existing

        json_response = self.client.person.enrichment(**params).json()
        if json_response["status"] != 200:
            raise ValueError(f"Error in API call: {json_response}")

        response = JsonPersonResponse(**json_response)
        if response.status != 200:
            return []
        data = response.data
        people = []
        if not isinstance(data, list):
            data_list = [data]
        else:
            data_list = data
        for d in data_list:
            peeps = Person(**d)
            pw = PersonWrapper(
                person=peeps,
                likelihood=response.likelihood,
                dataset_version=response.dataset_version,
            )
            people.append(pw)
            self.existing_people.append(pw)

        if self.storage_loc:
            for pw in people:
                ## make an id from name and email
                pid = pw.person.full_name
                ## normalize the id
                pid = pid.replace(" ", "_")
                js = pw.model_dump(mode="json")
                js["zother"] = {"email": params["email"][0]}
                with open(f"{self.storage_loc}/{pid}.json", "w") as f:
                    f.write(json.dumps(js))

        return people

