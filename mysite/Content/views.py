from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Propuestas(request):
    return render(request, 'propuestas.html')

def about(request):
    return HttpResponse('About')

def feedback(request):
    return render(request, 'encuesta.html')