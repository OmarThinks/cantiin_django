from pprint import pprint as pp

from urllib.parse import urlparse



trusted_origins = [
    "https://cantiin.com",
    "https://www.example.com",
    "https://www.cantiin-react.com",
    "http://cantiin.com",
    "http://www.example.com",
    "http://www.cantiin-react.com",
    "http://localhost:8080",
    "http://localhost:3080",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "https://cantiin.d3thsty4rzma1i.amplifyapp.com",
    "http://cantiin.d3thsty4rzma1i.amplifyapp.com",
    "https://dev.d2ehwgu036lbhk.amplifyapp.com/",
    "http://dev.d2ehwgu036lbhk.amplifyapp.com/"
]



#http://localhost:3000

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]



def get_origin(request):
    origin = request.headers.get("Referer", request.headers.get("Origin", "*"))
    if (origin == "*"):
        return "*"
    pure_origin = urlparse(origin).scheme + "://"+urlparse(origin).netloc
    #print(pure_origin)
    if (pure_origin in trusted_origins):
        #print("found the origin")
        return pure_origin
    #print("can not find the origin")
    return "*"
        




class CORSMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True) # Disable CSRF
        #pp(request.headers)
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] =  get_origin(request)
        response["Access-Control-Allow-Headers"] =  ",".join(CORS_ALLOW_HEADERS)
        response["Access-Control-Allow-Credentials"] =  "true"
        return response
