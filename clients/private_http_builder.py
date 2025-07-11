from httpx import Client
from pydantic import BaseModel, EmailStr
from functools import lru_cache
from clients.authentication.authentication_client import get_authentication_client, LoginRequestSchema


class AuthenticationUserSchema(BaseModel, frozen=True):
    email: EmailStr
    password: str


@lru_cache
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authentication_client = get_authentication_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)
    access_token = login_response.token.access_token

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {access_token}"}
    )
