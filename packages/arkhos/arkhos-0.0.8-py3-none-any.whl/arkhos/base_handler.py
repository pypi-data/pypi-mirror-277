from collections import defaultdict
import datetime, json, logging, time

from arkhos.http import HttpResponse, JsonResponse, render, render_static

from arkhos import _global


def base_handler(event, context=""):
    start_time = time.time()

    request = Request(event)
    response = {}

    try:
        if request.path.startswith("/static/"):
            response = render_static(request.path)
        else:
            user_handler = get_user_handler()
            response = user_handler(request)

        if isinstance(response, (HttpResponse, JsonResponse)):
            response = response.serialize()
        else:
            response = JsonResponse(
                {
                    "error": f"Server Error - arkhos_handler returned an invalid response, returned {type(response).__name__} "
                },
                status=500,
            ).serialize()
    except:
        logging.exception("User handler error")
        response = JsonResponse({"error": "500 Server Error"}, status=500).serialize()

    finally:
        end_time = time.time()
        duration = end_time - start_time
        response["arkhos_duration"] = {
            "start_time": start_time,
            "end_time": end_time,
            "duration": duration,
        }

    return response


def get_user_handler():
    """This returns the user's handler"""

    if __name__ == "__main__":
        pass  # script, running in lambda
    else:  # module, running locally
        import os, sys

        sys.path.append(os.getcwd())

    from main import arkhos_handler

    return arkhos_handler


class Request:
    """Represents a request"""

    def __init__(self, lambda_event):
        self.method = lambda_event.get("method")
        self.headers = lambda_event.get("headers", {})
        self.GET = lambda_event.get("GET", {})
        self.parsed_json = False

        self.path = lambda_event.get("path")

    @property
    def json(self):
        """Parse the request body. This will throw an error if request.body
        isn't valid json"""
        self.parsed_json = self.parsed_json or json.loads(self.POST)
        return self.parsed_json

    def __str__(self):
        object_values = {
            "method": self.method,
            "headers": self.headers,
            "GET": self.GET,
            # "body": self.body,
        }
        return object_values
