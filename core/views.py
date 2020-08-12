from django.shortcuts import render
from .forms import ContactoForm


# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

def postres(request):
    return render(request, 'core/postres.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "¡Tu mensaje ha sido enviado correctamente!"
    return render(request, 'core/contacto.html', data)

def sabores(request):
    return render(request, 'core/sabores.html')

def historia(request):
    return render(request, 'core/historia.html')