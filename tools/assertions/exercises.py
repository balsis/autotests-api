from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: CreateExerciseResponseSchema):
    """
    Проверяет, что ответ на создание задания соответствует запросу.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.exercise.title, name="title")
    assert_equal(request.description, response.exercise.description, name="description")
    assert_equal(request.max_score, response.exercise.max_score, name="max_score")
    assert_equal(request.min_score, response.exercise.min_score, name="min_score")
    assert_equal(request.estimated_time, response.exercise.estimated_time, name="estimated_time")
    assert_equal(request.course_id, response.exercise.course_id, name="course_id")
    assert_equal(request.order_index, response.exercise.order_index, name="order_index")
