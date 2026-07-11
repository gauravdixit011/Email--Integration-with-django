from datetime import datetime

from django.http import HttpResponse

class SimpleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("Middleware Initialized")

    def __call__(self, request):
        # Code before view
        print("Before View")
        print(f"""
------------------------------
Time   : {datetime.now()}
Method : {request.method}
Path   : {request.path}
------------------------------
""")
        

        response = self.get_response(request)

        # Code after view
        print("After View")

        return response