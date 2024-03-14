from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:vehicle_id>/', views.detail, name="detail"),
    path('create/', views.create_vehicle, name="create_vehicle"),
    path('<int:vehicle_id>/edit/', views.edit_vehicle, name="edit_vehicle"),
    path('delete/<int:vehicle_id>/', views.delete, name="delete")
]