from django import forms 
from .models import MyModel

class MyModelforms(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name','description']
