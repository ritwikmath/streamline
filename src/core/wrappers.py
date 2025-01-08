from functools import wraps
import json


def parse_event(method):
    @wraps(method)
    def inner_function(self, *args):
        try:
            event, context = args[0], args[1]
            request_context = event["requestContext"]
            http_method = request_context["http"]["method"]
            http_path = request_context["http"]["path"]
            body = json.loads(event.get("body"))

            return method(self, http_path, http_method, body)
        except Exception as ex:
            print(ex)
            return "Something went wrong"

    return inner_function
