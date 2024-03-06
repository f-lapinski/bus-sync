from django.http import HttpResponse


def index(request):
    return HttpResponse("There are vehicles")
