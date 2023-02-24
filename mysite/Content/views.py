from django.shortcuts import render
from django.http import HttpResponse
from .models import Propuesta

# Create your views here.

def Propuestas(request):
    return render(request, 'propuestas.html')

def about(request):
    return HttpResponse('About')

def feedback(request):
    if request.method == 'POST':
        Title = request.POST.get('Title')
        Description = request.POST.get('description')
        Grade = None
        email = None
        if request.POST.get('email') is not None: 
            email = request.POST.get('email')
        if request.POST.get('grado') is not None:
            Grade = request.POST.get('grado')
        NewProposal = Propuesta.objects.create(
            Title = Title,
            Description = Description,
            Grado  = Grade,
            Email = email
        )
        NewProposal.save()

    return render(request, 'encuesta.html')