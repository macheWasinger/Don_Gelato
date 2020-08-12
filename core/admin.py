from django.contrib import admin
from .models import Contacto

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'mail', 'mensaje']

admin.site.register(Contacto, ContactoAdmin)
# Register your models here.
