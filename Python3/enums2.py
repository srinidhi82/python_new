from enum import Enum
class HTTPStatus(Enum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

def get_error_message(status_code):
        if status_code == HTTPStatus.NOT_FOUND:
            return "Page not found"
        elif status_code == HTTPStatus.SERVER_ERROR:
            return "Internal server error"
        elif status_code == HTTPStatus.BAD_REQUEST:
            return "Bad request sent"
        elif status_code == HTTPStatus.OK:
           return "Request successful"
        else:
            return "Unknown status code"
status_code = 404
if HTTPStatus.NOT_FOUND.value == status_code:
    print("Matched!")

# Simulate receiving a status code from an API
received_status = HTTPStatus.NOT_FOUND
print(received_status)

message = get_error_message(received_status)


print(f"Response message: {message}")
