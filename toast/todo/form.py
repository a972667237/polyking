from django import forms
 
class AddForm(forms.Form):
    a = forms.CharField(max_length=40,label='新事项')