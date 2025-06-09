import httpx

from tools.fakers import get_random_email


create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post(url="http://localhost:8000/api/v1/users",
                                  json=create_user_payload)
create_user_response_data = create_user_response.json()
print('create user data:', create_user_response_data)

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post(url="http://localhost:8000/api/v1/authentication/login",
                            json=login_payload)
login_response_data = login_response.json()
print('login data:', login_response_data)

access_token = login_response_data["token"]["accessToken"]
user_id = create_user_response_data["user"]["id"]
update_user_headers = {"Authorization": f"Bearer {access_token}"}

update_user_payload = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

update_user_response = httpx.patch(url=f"http://localhost:8000/api/v1/users/{user_id}",
                                   headers=update_user_headers,
                                   json=update_user_payload)
update_user_response_data = update_user_response.json()
print('update user data:', update_user_response_data)
