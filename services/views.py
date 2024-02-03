from django.shortcuts import render, get_object_or_404
from .models import Service

def index(request):
    """render the home page"""
    
    context = {}
    return render(request, "services/index.html", context)

def services(request):
    """fetch all services"""
    
    services = Service.objects.all()
    context = {"services": services}
    return render(request, "services/services.html", context)

def service(request, slug):
    """fetch each service"""
    
    service = get_object_or_404(Service, slug=slug)
    sub_services = service.subservice_set.all()
    context = {"service": service, "sub_services": sub_services}
    return render(request, "services/service.html", context)
