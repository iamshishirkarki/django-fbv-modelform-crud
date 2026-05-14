from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model= User
        # fields= ['name', 'email', 'password']          for customizing what what model fields we want
        fields= '__all__' #if we need all then we can simple use __all__ that will add all the model fields.

        widgets= {
            'name': forms.TextInput(attrs= {'class': 'form-control'}),
            'email': forms.EmailInput(attrs= {'class': 'form-control'}),
            'password': forms.PasswordInput(render_value= True , attrs= {'class': 'form-control'}),
            
            # render_value= TrueThis will show the Password in the EDIT Section
        }