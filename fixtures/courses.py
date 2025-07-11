import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(user=function_user.authentication_user)


@pytest.fixture
def function_course(courses_client: CoursesClient, function_user: UserFixture, function_file: FileFixture):
    request = CreateCourseRequestSchema()
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)
