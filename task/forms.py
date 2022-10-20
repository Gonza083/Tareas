from dataclasses import fields
from django.forms import ModelForm
from .models import Task
from django import forms

class TaskForm(ModelForm):
    class Meta():
        model = Task
        fields= ['title', 'descripcion', 'importan']
        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Write a title"}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder':"Write a description"}),
            'importan': forms.CheckboxInput(attrs={'class':'form-check-input text-center'}),
        }