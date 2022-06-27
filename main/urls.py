from django.urls import path
from . import views
from .views import Contactos;
urlpatterns = [
    
    path("contact/", Contactos.as_view(), name='Contactos'),
]