from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle


def index(request):
    # Retrieve all vehicles
    vehicles = Vehicle.objects.all()

    # Number of vehicles to display per page
    per_page = 25

    # Create a paginator object
    paginator = Paginator(vehicles, per_page)

    # Get the current page number from the request
    page_number = request.GET.get('page')

    # Get the vehicles for the requested page
    page_obj = paginator.get_page(page_number)

    # Pass the page object to the template
    return render(request, 'vehicles/all_vehicles.html', {'page_obj': page_obj})


def detail(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    return render(request, 'vehicles/vehicle_details.html', {'vehicle': vehicle})


def create_vehicle(request):
    if request.method == 'POST':
        inv_number = request.POST.get('inv_number')
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        register_number = request.POST.get('register_number')

        # Create a new Vehicle object
        Vehicle.objects.create(inv_number=inv_number, brand=brand, model=model, register_number=register_number)

        return redirect('/vehicles/')  # Redirect to a success page or another URL

    return render(request, 'vehicles/forms/create_form.html')


def edit_vehicle(request, vehicle_id):
    # Retrieve the Vehicle object to be edited
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

    if request.method == 'POST':
        # If form is submitted, process the form data
        vehicle.inv_number = request.POST['inv_number']
        vehicle.brand = request.POST['brand']
        vehicle.model = request.POST['model']
        vehicle.register_number = request.POST['register_number']
        vehicle.save()
        # Redirect to a success URL or show a success message
        return redirect(f'/vehicles/{vehicle_id}')

    # If it's a GET request, render the form with the existing data
    return render(request, 'vehicles/forms/edit_form.html', {'vehicle': vehicle})


def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('/vehicles/')
    return render(request, 'vehicles/vehicle_delete.html', {'vehicle': vehicle})