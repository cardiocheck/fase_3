from django.urls import path
from formulario import views

urlpatterns = [
    path('', views.index, name='index'),
    path('conocenos/', views.conocenos, name='conocenos'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),
]
