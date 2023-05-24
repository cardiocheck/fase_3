from django.shortcuts import render
from .forms import ContactoForm

def index(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'formulario/confirmacion.html')
    else:
        form = ContactoForm()
    
    return render(request, 'formulario/index.html', {'form': form})


# CONTROLADORES ADICIONALES
def conocenos(request):
    return render(request, 'formulario/conocenos.html')

def contacto(request):
    return render(request, 'formulario/contacto.html')

def servicios(request):
    return render(request, 'formulario/servicios.html')
