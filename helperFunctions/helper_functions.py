import os
import requests
import random
import string
import json


class RequestFunctions:
    def __init__(self) -> None:
        self.base_url = "https://gorest.co.in"
        self.auth_token = os.environ["TOKEN"]

    # Generate random email id
    def generate_random_emailid(self) -> string:
        suffix = "@ktautomation.com"
        prefix = "".join(random.choice(string.ascii_lowercase) for _ in range(10))
        return f"{prefix}{suffix}"

    def get_request(self, url: string) -> json:
        print("\n🤖 Making a GET Request")
        url = self.base_url + url
        print(f"🔗 GET URL = {url}")

        headers = {"Authorization": self.auth_token}
        return requests.get(url=url, headers=headers)

    def post_request(self, url: string) -> json:
        print("\n🤖 Making a POST Request")
        url = self.base_url + url
        print(f"🔗 POST URL = {url}")
        headers = {"Authorization": self.auth_token}
        email_id = self.generate_random_emailid()
        data = {
            "name": "black wall",
            "email": email_id,
            "gender": "male",
            "status": "active",
        }
        return requests.post(url=url, headers=headers, json=data)

    def put_request(self, url: string, user_id: int) -> json:
        print("\n🤖 Making a PUT Request")
        url = f"{self.base_url}{url}{user_id}"
        print(f"🔗 PUT URL = {url}")

        headers = {"Authorization": self.auth_token}
        email_id = self.generate_random_emailid()

        data = {
            "id": user_id,
            "name": "QA Automation put call",
            "email": email_id,
        }

        return requests.put(url=url, json=data, headers=headers)

    def delete_request(self, url: string, user_id: int):
        print("\n🤖 Making a DELETE Request")
        url = f"{self.base_url}{url}{user_id}"
        print(f"🔗 DELETE URL = {url}")

        headers = {"Authorization": self.auth_token}
        return requests.delete(
            url=url,
            headers=headers,
        )
