from django.urls import path
from . import views
"""No olvidarse de importar todas las vistas creadas!!!!"""
from .views import principal

urlpatterns = [

path('', principal, name='home'),

 
]
