from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:vehicle_id>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('update/<int:vehicle_id>/', views.update, name="update"),
    path('delete/<int:vehicle_id>/', views.delete, name="delete")
]