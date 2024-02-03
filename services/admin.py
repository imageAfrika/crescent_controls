from django.contrib import admin
from .models import Service, SubService


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('service_name',)}
    
class SubServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('sub_service_name',)}
    
    
admin.site.register(Service, ServiceAdmin)
admin.site.register(SubService, SubServiceAdmin)
