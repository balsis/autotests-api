import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient
from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(
        exercises_client: ExercisesClient,
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture
) -> ExerciseFixture:
    request = CreateExerciseRequestSchema()
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
