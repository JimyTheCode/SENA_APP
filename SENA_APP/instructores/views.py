from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from instructores.models import Instructor
from instructores.forms import InstructorForm


# VISTA DE LISTA DE INSTRUCTORES
def instructores(request):
    instructores = Instructor.objects.all().values()
    context = {
        'instructores': instructores
    }
    return render(request, "lista_instructores.html", context)    


# VISTA DE DETALLE DE INSTRUCTOR
def detalle_instructor(request, instructor_id):
    instructor = Instructor.objects.get(id=instructor_id)
    template = loader.get_template('detalle_instructores.html')
    context = {
        'instructor': instructor,
    }
    return HttpResponse(template.render(context, request))


# VISTAS BASADAS EN CLASES - CRUD INSTRUCTOR

# CREATE - INSTRUCTOR
class InstructorCreateView(generic.CreateView):
    """Vista para crear un nuevo instructor"""
    model = Instructor
    form_class = InstructorForm
    template_name = 'agregar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el instructor"""
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre_completo()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# UPDATE - INSTRUCTOR
class InstructorUpdateView(generic.UpdateView):
    """Vista para actualizar un instructor existente"""
    model = Instructor
    form_class = InstructorForm
    template_name = 'editar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    pk_url_kwarg = 'instructor_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre_completo()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# DELETE - INSTRUCTOR
class InstructorDeleteView(generic.DeleteView):
    """Vista para eliminar un instructor"""
    model = Instructor
    template_name = 'eliminar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    pk_url_kwarg = 'instructor_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        instructor = self.get_object()
        messages.success(
            request,
            f'El instructor {instructor.nombre_completo()} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)