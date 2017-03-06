from django import forms
from .models import Things 

class AddForm(forms.ModelForm):
    thing_text = forms.CharField(max_length=40,label='新事项')
    class Meta:
        model = Things
        fields = ['thing_text']
