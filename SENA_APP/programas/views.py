from django.shortcuts import render, get_object_or_404
from .models import Programa

# Create your views here.
def main(request):
    return render(request, "main.html")

def programas(request):
    lista_programas = Programa.objects.all()
    context = {
        'programas': lista_programas,
    }
    return render(request, 'lista_programas.html', context)

def detalle_programa(request, id_programa):
    programa = get_object_or_404(Programa, id=id_programa)
    context = {
        'programa': programa,
    }
    return render(request, 'detalles_programa.html', context)