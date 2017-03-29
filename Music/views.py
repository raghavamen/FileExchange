from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> This is the place for Exchange of Music </h1>")


