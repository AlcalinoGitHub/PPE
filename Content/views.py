from django.shortcuts import render
from django.http import HttpResponse
from .models import Propuesta
from django.contrib import messages

# Create your views here.

def Propuestas(request):
    return render(request, 'propuestas.html')

def about(request):
    return render(request,'about.html')

def feedback(request):
    if request.method == 'POST':
        Title = request.POST.get('Title')
        Description = request.POST.get('description')
        Grade = None
        email = None

        if CorrectWording(Title) is not None:
            messages.info(request, f'No se admiten palabras altisonantes')
            return render(request, 'encuesta.html')
        if CorrectWording(Description) is not None:
            messages.info(request, f'No se admiten palabras altisonantes')
            return render(request, 'encuesta.html')

        if request.POST.get('email') is not None: 
            email = request.POST.get('email')
        if request.POST.get('grado') is not None:
            Grade = request.POST.get('grado')
        else:
            Grade = -1
        NewProposal = Propuesta.objects.create(
            Title = Title,
            Description = Description,
            Grado  = Grade,
            Email = email
        )
        NewProposal.save()
        messages.info(request, 'La sugerencia ha sido enviada!')
    return render(request, 'encuesta.html')


def CorrectWording(texto):
    altisonantes =  ["verga", "puto", "puta", "hijo de", "pinche", "chinga", "chinguen", "chingo"]
    texto = texto.lower()
    texto = texto.split(' ')
    for i in altisonantes:
        if i in texto:
            return (i)
    return None