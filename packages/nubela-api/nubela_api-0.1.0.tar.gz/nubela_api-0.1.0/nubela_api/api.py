import glob
import json
import os
from dataclasses import dataclass, field
from typing import Optional

import requests
import uuid


@dataclass
class NubelaAPI:
    api_key: str
    storage_loc: Optional[str] = None
    existing_people: list[dict] = field(default_factory=list)

    def __post_init__(self):
        if not self.api_key:
            raise ValueError("api_key is required")
        if self.storage_loc:
            self.storage_loc = os.path.expanduser(self.storage_loc)
            os.makedirs(self.storage_loc, exist_ok=True)
            self.existing_people = self.load_people(self.storage_loc)

    def load_people(self, storage_loc: str) -> list[dict]:
        """Load existing people from a directory of json files"""
        files = glob.glob(f"{storage_loc}/*.json")
        ppl = []
        for file in files:
            with open(file, "r") as f:
                data = json.load(f)
                ppl.append(data)
        return ppl

    def find_via_linkedin(self, linkedin_url: str) -> Optional[dict]:
        for person in self.existing_people:
            try:
                if person["zother"]["linkedin_url"] == linkedin_url:
                    return person
                ## person["experiences"]["starts_at"]
                # Sort by experiences and start_at
                # for experience in person["experiences"]:
                #     if experience["company"] and experience["company"]["linkedin_url"] == linkedin_url:
                #         return person

            except:
                pass
        return None

    def enrich_via_linkedin(self, linkedin_url: str, skip_if_exists: bool = True) -> dict:
        if skip_if_exists:
            person = self.find_via_linkedin(linkedin_url)
            if person:
                return person
        headers = {"Authorization": "Bearer " + self.api_key}
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        params = {
            "linkedin_profile_url": linkedin_url,
            "extra": "include",
            "github_profile_id": "include",
            "facebook_profile_id": "include",
            "twitter_profile_id": "include",
            "personal_contact_number": "include",
            "personal_email": "include",
            "inferred_salary": "include",
            "experience": "include",
            "skills": "include",
            "use_cache": "if-present",
            "fallback_to_cache": "on-error",
        }
        response = requests.get(api_endpoint, params=params, headers=headers)

        data = response.json()

        if self.storage_loc:
            try:
                person_id = data["full_name"] + "_" + data.get("linkedin_url","").split("/")[-1]
                ## remove /
                person_id = person_id.replace("/", "_")
            except:
                person_id = str(uuid.uuid4().hex)
            data["zother"] = {"linkedin_url": linkedin_url}
            with open(f"{self.storage_loc}/{person_id}.json", "w") as f:
                json.dump(data, f)
        json_string = json.dumps(data, indent=4)

        print("Response Body:", json_string)
        return data

