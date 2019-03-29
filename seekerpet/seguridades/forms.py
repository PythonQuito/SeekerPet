from django import forms
from django.contrib.auth.models import User
from seekerpet.seguridades import models


class RegistroForm(forms.ModelForm):

    telefono = forms.CharField(max_length=13, required=True)
    direccion = forms.CharField(max_length=255, required=False)
    ciudad = forms.ModelChoiceField(queryset=models.Ciudad.objects.none())

    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'date_joined']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.PasswordInput()
        self.fields['ciudad'].queryset = models.Ciudad.objects.all()

    
    def clean_telefono(self):
        if len(self.cleaned_data.get('telefono')) < 9:
            raise forms.ValidationError('Menor de 9 digitos')
        return self.cleaned_data.get('telefono')