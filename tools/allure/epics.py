from enum import Enum


class AllureEpic(str, Enum):
    LMS = "LMS Service"
    STUDENT = "Student service"
    ADMINISTRATION = "Administration service"
   