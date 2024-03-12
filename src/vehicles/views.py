from django.http import HttpResponse
from django.shortcuts import render

from .models import Vehicle


def index(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/all_vehicles.html', {'vehicles': vehicles})


def detail(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    return render(request, 'vehicles/vehicle_details.html', {'vehicle': vehicle})


def create(request):
    return None


def update(request):
    return None


def delete(request):
    return None