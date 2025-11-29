from django.shortcuts import render
from .models import Aprendiz
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def main(request):
    return render(request, "main.html")

def aprendices(request):
    aprendices = Aprendiz.objects.all().values()
    context = {
        'aprendices': aprendices
    }
    return render(request, "lista_aprendices.html", context)    

def detalle_aprendiz(request, id_aprendiz):
  aprendiz = Aprendiz.objects.get(id=id_aprendiz)
  template = loader.get_template('detalle_aprendiz.html')
  context = {
    'aprendiz': aprendiz,
  }
  return HttpResponse(template.render(context, request))

def inicio(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())