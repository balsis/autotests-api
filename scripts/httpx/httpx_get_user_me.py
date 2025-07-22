import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post(url = "http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

access_token = login_response_data["token"]["accessToken"]

users_me_headers = {"Authorization": f"Bearer {access_token}"}
users_me_response = httpx.get(url = "http://localhost:8000/api/v1/users/me", headers = users_me_headers)
users_me_response_data = users_me_response.json()

print("User response:", users_me_response_data)
print("Status Code:", users_me_response.status_code)


