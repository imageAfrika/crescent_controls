from django.db import models

class Service(models.Model):
    service_name = models.CharField(max_length = 250)
    slug = models.SlugField()
    intro = models.TextField(blank = True)
    service_image = models.ImageField(upload_to='images/', blank=True, null=True)
    service_details = models.TextField()
    
    """String rep of the model"""
    def __str__(self):
        return self.service_name

class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete = models.CASCADE)
    sub_service_name = models.CharField(max_length = 250)
    slug = models.SlugField()
    info = models.TextField(blank = True)
    sub_service_image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    """String rep of the model"""
    def __str__(self):
        return self.sub_service_name
    
        """
        <!-- <li><a href="{% url 'services:about' %}">About</a></li> -->
        <!-- <li><a href="{% url 'products:all_products' %}">Products</a></li> -->
        <!-- <li><a href="{% url 'projects:all_projects' %}">Projects</a></li>
        <li><a href="{% url 'projects:all_clients' %}">Clients</a></li> -->
        """
