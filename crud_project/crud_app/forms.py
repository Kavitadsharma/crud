# crud_app/forms.py

from django import forms

class ItemForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
