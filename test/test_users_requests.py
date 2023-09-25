import json


def test_get_request(helper):
    res = helper.get_request("/public/v2/users/")
    assert res.status_code == 200
    json_data = res.json()
    json_str = json.dumps(json_data, indent=4)
    print(json_str)


def test_post_request(helper):
    global user_id
    res = helper.post_request("/public/v2/users/")
    json_data = res.json()
    print(json_data)
    assert res.status_code == 201
    assert json_data["name"] == "black wall"
    # assert json_data["email"] == email_id
    user_id = json_data["id"]


def test_put_request(helper):
    res = helper.put_request("/public/v2/users/", user_id)
    print(res.json())
    assert res.status_code == 200


def test_delete_request(helper):
    res = helper.delete_request("/public/v2/users/", user_id)
    print(res.status_code)
    print(".......... DELETED USER .........")
    assert res.status_code == 204
