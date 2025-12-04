from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('programas/', views.programas, name='lista_programas'),
    path('programas/<int:id_programa>/', views.detalle_programa, name='detalle_programas'),
]