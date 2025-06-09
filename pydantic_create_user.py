from pydantic import BaseModel, EmailStr, Field, constr, UUID4


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: UUID4
    email: EmailStr = Field(max_length=250)
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: EmailStr = Field(max_length=10)
    password: constr(min_length=1, max_length=250)
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema


