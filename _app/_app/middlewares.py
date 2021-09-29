class CORSMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #setattr(request, '_dont_enforce_csrf_checks', True) # Disable CSRF
        response = self.get_response(request)
        response['access-control-allow-origin'] = "*"
        response['access-control-allow-headers'] = "*"
        """["accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]"""
        return response