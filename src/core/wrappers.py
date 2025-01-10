from functools import wraps
import json
import traceback


def parse_event(controller):
    @wraps(controller)
    def inner_function(self, *args):
        try:
            event, context = args[0], args[1]
            request_context = event["requestContext"]
            http_method = request_context["http"]["method"]
            http_path = request_context["http"]["path"]
            body = None
            if (request_body := event.get("body")) is not None:
                body = json.loads(request_body)

            return controller(self, http_path, http_method, body)
        except Exception as ex:
            print(traceback.format_exc())
            return {
                "status_code": 500,
                "body": {
                    "message": "Something Went Wrong"
                }
            }

    return inner_function
