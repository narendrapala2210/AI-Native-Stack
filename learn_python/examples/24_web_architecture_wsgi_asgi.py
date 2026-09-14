"""
Python Concept Examples: 24. Web Architecture: WSGI, ASGI & Server Internals
Documentation Reference: ../24.web_architecture_wsgi_asgi.md
"""

import sys
import os

def example_1():
    """
    Example 1: Custom Minimal Routing Micro-Framework with WSGI
    """
    print("-" * 50)
    print("Running Example 1: Custom Minimal Routing Micro-Framework with WSGI")
    print("-" * 50)
    import json

    class MiniRouterWSGI:
        def __init__(self):
            self.routes = {}

        def route(self, path: str):
            def decorator(handler):
                self.routes[path] = handler
                return handler
            return decorator

        def __call__(self, environ, start_response):
            path = environ.get("PATH_INFO", "/")
            handler = self.routes.get(path)

            if handler:
                status = "200 OK"
                headers = [("Content-Type", "application/json")]
                body = json.dumps(handler(environ)).encode("utf-8")
            else:
                status = "404 Not Found"
                headers = [("Content-Type", "text/plain")]
                body = b"Route not found."

            start_response(status, headers)
            return [body]

    app = MiniRouterWSGI()

    @app.route("/api/ping")
    def ping_handler(environ):
        return {"message": "pong", "status": "UP"}

    # Simulate server call
    def mock_start_response(status, headers):
        print("Response Status:", status)

    response = app({"PATH_INFO": "/api/ping"}, mock_start_response)
    print("Response Body:", b"".join(response).decode())

def example_2():
    """
    Example 2: Asynchronous Server-Sent Events (SSE) Streaming with ASGI
    """
    print("-" * 50)
    print("Running Example 2: Asynchronous Server-Sent Events (SSE) Streaming with ASGI")
    print("-" * 50)
    import asyncio

    async def sse_event_stream_app(scope, receive, send):
        assert scope["type"] == "http"

        # 1. Send SSE Headers
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text/event-stream"],
                [b"cache-control", b"no-cache"],
            ]
        })

        # 2. Stream 3 real-time ticks
        for i in range(1, 4):
            msg = f"data: tick #{i}\n\n".encode("utf-8")
            await send({
                "type": "http.response.body",
                "body": msg,
                "more_body": True if i < 3 else False
            })
            await asyncio.sleep(0.01)

def example_3():
    """
    Example 3: Request Timing & Authentication Middleware Pipeline
    """
    print("-" * 50)
    print("Running Example 3: Request Timing & Authentication Middleware Pipeline")
    print("-" * 50)
    class TimingAndAuthMiddleware:
        def __init__(self, app, valid_token: str = "Bearer secret123"):
            self.app = app
            self.valid_token = valid_token

        def __call__(self, environ, start_response):
            import time
            start_time = time.perf_counter()

            auth_header = environ.get("HTTP_AUTHORIZATION", "")
            if auth_header != self.valid_token:
                start_response("401 Unauthorized", [("Content-Type", "text/plain")])
                return [b"Missing or invalid Bearer token."]

            def custom_start_response(status, headers, exc_info=None):
                duration = (time.perf_counter() - start_time) * 1000
                headers.append(("X-Response-Time-Ms", f"{duration:.2f}"))
                return start_response(status, headers, exc_info)

            return self.app(environ, custom_start_response)

    wrapped = TimingAndAuthMiddleware(app)
    res_unauth = wrapped({}, lambda s, h, e=None: print("Unauth test:", s))
    print("Unauth output:", b"".join(res_unauth).decode())

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 24. Web Architecture: WSGI, ASGI & Server Internals Examples")
    print("=" * 60)

    try:
        example_1()
    except Exception as exc:
        print(f"Notice in Example 1: {exc}")
    print()
    try:
        example_2()
    except Exception as exc:
        print(f"Notice in Example 2: {exc}")
    print()
    try:
        example_3()
    except Exception as exc:
        print(f"Notice in Example 3: {exc}")
    print()
    print("=" * 60)
    print("Completed 24. Web Architecture: WSGI, ASGI & Server Internals Examples")
    print("=" * 60)
