from functools import wraps
import json


def parse_event(func):
    @wraps(func)
    def inner_function(*args):
        event, context = args[1], args[2]
        request_context = event["requestContext"]
        http_method = request_context["http"]["method"]
        http_path = request_context["http"]["path"]
        body = json.loads(event.get("body"))

        return func(args[0], http_path, http_method, body)    

    return inner_function
