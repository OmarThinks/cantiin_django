from pprint import pprint as pp

from urllib.parse import urlparse






trusted_origins = [
    "https://cantiin.com",
    "https://www.example.com",
    "http://cantiin.com",
    "http://www.example.com",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "https://cantiin.d3thsty4rzma1i.amplifyapp.com",
    "http://cantiin.d3thsty4rzma1i.amplifyapp.com"
]


#http://localhost:3000


def get_origin(request):
    origin = request.headers.get("Referer", request.headers.get("Origin", "*"))
    if (origin == "*"):
        return "*"
    pure_origin = urlparse(origin).scheme + "://"+urlparse(origin).netloc
    print(pure_origin)
    if (pure_origin in trusted_origins):
        print("found the origin")
        return pure_origin
    print("can not find the origin")
    return "*"
        




class CORSMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True) # Disable CSRF
        #pp(request.headers)
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] =  get_origin(request)
        return response
