from django import forms
from .models import Add



class AddForm(forms.ModelForm):
    
    class Meta:
        model = Add
        fields = ['name','branch','language','field','technical_language']
