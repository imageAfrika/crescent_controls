from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
    # Renders the home page
    path('', views.index, name="index"),
    
    # shows all services
    path('services/', views.services, name="all_services"),
    
    # shows each service with its content
    path('services/<slug:slug>/', views.service, name="service"),
]