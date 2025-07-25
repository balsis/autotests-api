import grpc

from scripts.grpc_client_server import course_service_pb2
import course_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="api-course"))


if __name__ == "__main__":
    print(response)
