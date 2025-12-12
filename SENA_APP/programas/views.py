from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Programa
from .forms import ProgramaForm

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


# VISTAS BASADAS EN CLASES - CRUD PROGRAMA

# CREATE - PROGRAMA
class ProgramaCreateView(generic.CreateView):
    """Vista para crear un nuevo programa"""
    model = Programa
    form_class = ProgramaForm
    template_name = 'agregar_programa.html'
    success_url = reverse_lazy('programas:lista_programas')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el programa"""
        messages.success(
            self.request,
            f'El programa {form.instance.nombre} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# UPDATE - PROGRAMA
class ProgramaUpdateView(generic.UpdateView):
    """Vista para actualizar un programa existente"""
    model = Programa
    form_class = ProgramaForm
    template_name = 'editar_programa.html'
    success_url = reverse_lazy('programas:lista_programas')
    pk_url_kwarg = 'programa_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f'El programa {form.instance.nombre} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# DELETE - PROGRAMA
class ProgramaDeleteView(generic.DeleteView):
    """Vista para eliminar un programa"""
    model = Programa
    template_name = 'eliminar_programa.html'
    success_url = reverse_lazy('programas:lista_programas')
    pk_url_kwarg = 'programa_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        programa = self.get_object()
        messages.success(
            request,
            f'El programa {programa.nombre} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)