from django.shortcuts import render
from .forms import ContactoForm, InfoMedicaForm

def index(request):
    if request.method == 'POST':
        form_contacto = ContactoForm(request.POST)
        form_medico = InfoMedicaForm(request.POST)
        if form_contacto.is_valid() and form_medico.is_valid():
            # Procesar los datos de ambos formularios
            # ...
            return render(request, 'formulario/confirmacion.html')
    else:
        form_contacto = ContactoForm()
        form_medico = InfoMedicaForm()

    return render(request, 'formulario/index.html', {'form_contacto':form_contacto, 'form_medico':form_medico})

# CONTROLADORES ADICIONALES
def conocenos(request):
    return render(request, 'formulario/conocenos.html')

def contacto(request):
    return render(request, 'formulario/contacto.html')

def servicios(request):
    return render(request, 'formulario/servicios.html')
