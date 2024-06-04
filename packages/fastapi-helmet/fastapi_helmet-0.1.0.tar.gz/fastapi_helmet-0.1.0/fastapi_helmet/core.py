from starlette.responses import Response


class HelmetCore:
    def __init__(self, **options):
        self.options = options

    def set_headers(self, response: Response):
        headers = {
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
            "Referrer-Policy": "no-referrer",
            "Content-Security-Policy": "default-src 'self'",
            "Strict-Transport-Security": "max-age=63072000; includeSubDomains",
            "Expect-CT": "max-age=86400, enforce",
        }
        for header, value in headers.items():
            if self.options.get(header, True):
                response.headers[header] = value
        custom_headers = self.options.get("custom_headers", {})
        for header, value in custom_headers.items():
            response.headers[header] = value
