from django import forms
from django.forms import widgets

class NoteForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Имя: ')
    mail = forms.EmailField(required=True, label='Email: ')
    text = forms.CharField(max_length= 2000, required=True, label='Текст', widget=forms.Textarea)

