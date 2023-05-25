from django import forms

class ContactoForm(forms.ModelForm):

    # info básica
    nombre = forms.CharField(label='Nombre', required=True)
    apellido = forms.CharField(label='Apellido', required=True)
    telefono = forms.IntegerField(label='Teléfono', required=True)
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput)
    dni = forms.IntegerField(label='DNI', required=True)


class InfoMedicaForm(forms.ModelForm):

    SEXO = ( ('option1', 'Masculino'), ('option2', 'Femenino'), ('option3', 'Otro') )
    SI_O_NO = ( ('option1', 'Si'),('option2', 'No') )

    edad = forms.IntegerField(label='Edad', required=True)
    peso = forms.IntegerField(label='Peso (kg)', required=True)
    altura = forms.IntegerField(label='Altura (cm)', required=True)
    sexo = forms.MultipleChoiceField(choices=SEXO, widget=forms.RadioSelect, required=True, label='Sexo')
    fumador = forms.MultipleChoiceField(choices=SI_O_NO, widget=forms.RadioSelect, required=True, label='¿Es fumador?')
    alcoholico = forms.MultipleChoiceField(choices=SI_O_NO, widget=forms.RadioSelect, required=True, label='¿Consume alcohol?')
    actividad_fisica = forms.MultipleChoiceField(choices=SI_O_NO, widget=forms.RadioSelect, required=True, label='¿Realiza actividad física?')
        