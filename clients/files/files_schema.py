from pydantic import BaseModel, HttpUrl, Field, FilePath

from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание файла.
    """
    file: FileSchema


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(default_factory=lambda: f'{fake.uuid4()}.png')
    directory: str = Field(default='tests')
    upload_file: FilePath


class GetFileResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос файла.
    """
    file: FileSchema
