from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('aprendices/', views.aprendices, name='lista_aprendices'),
    path('aprendices/aprendiz/<int:id_aprendiz>/', views.detalle_aprendiz, name='detalle_aprendiz'),
]
