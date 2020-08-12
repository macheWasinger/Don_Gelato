from django.urls import path
from .views import inicio, postres, contacto, sabores, historia

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('postres/', postres, name="postres"),
    path('contacto/', contacto, name="contacto"),
    path('sabores/', sabores, name="sabores"),
    path('historia/', historia, name="historia"),
]
