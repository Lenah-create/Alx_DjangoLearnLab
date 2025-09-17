# LibraryProject/middleware.py

class ContentSecurityPolicyMiddleware:
    """
    Middleware to set Content Security Policy (CSP) headers.
    Helps prevent XSS attacks by restricting sources for scripts, styles, images, etc.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # CSP header
        response['Content-Security-Policy'] = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self'; "
            "font-src 'self'; "
        )
        return response
