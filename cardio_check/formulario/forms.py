from django import forms

class InfoContactoForm(forms.Form):

    # info básica
    nombre = forms.CharField(label='Nombre', required=True)
    apellido = forms.CharField(label='Apellido', required=True)
    telefono = forms.CharField(label='Teléfono', required=True, max_length=9)
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput)
    dni = forms.CharField(label='DNI', required=True, max_length=9)


class InfoMedicaForm(forms.Form):

    SEXO = ( ('option1', 'Masculino'), ('option2', 'Femenino'), ('option3', 'Otro') )

    edad = forms.CharField(label='Edad', required=True)
    peso = forms.CharField(label='Peso (kg)', required=True)
    altura = forms.CharField(label='Altura (cm)', required=True)
    sexo = forms.MultipleChoiceField(choices=SEXO, widget=forms.RadioSelect, label='Sexo', required=True)
    fumador = forms.BooleanField(label='¿Es fumador?', required=False)
    alcoholico = forms.BooleanField(label='¿Consume alcohol?', required=False)
    actividad_fisica = forms.BooleanField(label='¿Realiza actividad física?', required=False)
