from django.shortcuts import render, redirect
from .forms import InfoContactoForm, InfoMedicaForm

def informacion_personal_view(request):
    if request.method == 'POST':
        form = InfoContactoForm(request.POST)
        if form.is_valid():
            # Almacenar los datos en la sesión
            request.session['informacion_personal'] = form.cleaned_data
            return redirect('informacion_medica')
    else:
        form = InfoContactoForm()
    return render(request, 'formulario/informacion_personal.html', {'form': form})

def informacion_medica_view(request):
    if request.method == 'POST':
        form = InfoMedicaForm(request.POST)
        if form.is_valid():
            # Almacenar los datos en la sesión
            request.session['informacion_medica'] = form.cleaned_data
            return redirect('confirmacion')
    else:
        form = InfoMedicaForm()
    return render(request, 'formulario/informacion_medica.html', {'form': form})

def gracias_view(request):
    # Obtener los datos de la sesión
    informacion_personal = request.session.get('informacion_personal')
    informacion_medica = request.session.get('informacion_medica')
    return render(request, 'formulario/confirmacion.html')





# CONTROLADORES ADICIONALES
def conocenos(request):
    return render(request, 'formulario/conocenos.html')

def contacto(request):
    return render(request, 'formulario/contacto.html')

def servicios(request):
    return render(request, 'formulario/servicios.html')
