from django.http import HttpResponse
from .models import Vehicle


def index(request):
    vehicles = Vehicle.objects.all()
    for vehicle in vehicles:
        return HttpResponse(str(vehicle))