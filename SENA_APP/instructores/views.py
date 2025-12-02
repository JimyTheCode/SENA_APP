from django.shortcuts import render, get_object_or_404
from .models import Instructor

# Create your views here.
def main(request):
    return render(request, "main.html")

def instructores(request):
    lista_instructores = Instructor.objects.all()
    context = {
        'instructores': lista_instructores
    }
    return render(request, 'lista_instructores.html', context)

def detalle_instructor(request, id_instructor):
    instructor = get_object_or_404(Instructor, id=id_instructor)
    context = {
        'instructor': instructor
    }
    return render(request, 'detalle_instructores.html', context)