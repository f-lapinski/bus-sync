from django.http import HttpResponse
from .models import Vehicle


def index(request):
    vehicles = Vehicle.objects.all()
    for vehicle in vehicles:
        return HttpResponse(str(vehicle))


def detail(request, vehicle_id):
    return HttpResponse(Vehicle.objects.get(id=vehicle_id))


def create(request):
    return None


def update(request):
    return None


def delete(request):
    return None