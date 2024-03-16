from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:vehicle_id>/', views.detail_vehicle, name="detail_vehicle"),
    path('create/', views.create_vehicle, name="create_vehicle"),
    path('<int:vehicle_id>/edit/', views.edit_vehicle, name="edit_vehicle"),
    path('<int:vehicle_id>/delete/', views.delete_vehicle, name="delete_vehicle")
]