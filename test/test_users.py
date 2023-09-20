import requests
import random
import json
import string
import os
from dotenv import load_dotenv


load_dotenv()
BASE_URL = "https://gorest.co.in"
auth_token = os.environ['TOKEN']
user_id = 0


# Generate random email id
def generate_random_emailid():
    suffix = "@ktautomation.com"
    prefix = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))    
    return f"{prefix}{suffix}"


# GET
def test_get_request():
    url = BASE_URL + "/public/v2/users/"
    print(f'get_url = {url}')
    headers = {"Authorization": auth_token}
    res = requests.get(url=url, headers=headers)
    assert res.status_code == 200
    json_data = res.json()
    json_str = json.dumps(json_data, indent=4)
    print(json_str)


# POST
def test_post_request():
    global user_id
    url = BASE_URL + "/public/v2/users/"
    email_id = generate_random_emailid()
    print(f'post_url = {url}')
    headers = {"Authorization": auth_token}
    data = {
        "name": "black wall",
        "email": email_id,
        "gender": "male",
        "status": "active"
        }
    res = requests.post(url=url, headers=headers, json=data)
    
    json_data = res.json()
    print(json_data)
    assert res.status_code == 201
    assert json_data["name"] == "black wall"
    assert json_data["email"] == email_id
    user_id = json_data["id"]


# PUT
def test_put_request():
    url = BASE_URL + f"/public/v2/users/{user_id}"
    print(f'put_url = {url}')
    headers = {"Authorization": auth_token}
    data = {
        "id": user_id,
        "name": "QA Automation put call",
        "email": generate_random_emailid(),
        }
    res = requests.put(url=url, json=data, headers=headers)
    print(res.json())
    assert res.status_code == 200
    

# DELETE
def test_delete_request():
    url = BASE_URL + f"/public/v2/users/{user_id}"
    print(f'DELETE url: {url}')
    header = {"Authorization": auth_token}
    res = requests.delete(url=url, headers=header)
    print(res.status_code)
    print(".......... DELETED USER .........")
    assert res.status_code == 204
    

# get_request()
# user_id = post_request()
# put_request(user_id)
# delete_request(user_id)