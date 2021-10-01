class CORSMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True) # Disable CSRF
        response = self.get_response(request)
        referer = request.headers.get("Referer","*")
        if(referer[-1]=="/"):
            referer = referer[:-1]
        response = self.get_response(request)
        response['access-control-allow-origin'] = referer
        response['access-control-allow-headers'] = "*,content-type,sessionid"
        response['Access-Control-Allow-Credentials'] = "true"
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
    
"""
        referer = request.headers.get("Referer","*")
        response = self.get_response(request)
# http://127.0.0.1:3000
# http://127.0.0.1:3000/
"""