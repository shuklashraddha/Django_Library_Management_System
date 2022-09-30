from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Book,student
from . import models

class BookForm(ModelForm):
    class Meta:
        model = models.Book
        
        fields = ('Bookname', 'Author', 'Describe', 'image')

        widgets = {
            'Bookname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bookname'}),
            'Author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'Describe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describe'}),
        }
    
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']


class StudentForm(forms.ModelForm):
    class Meta:
        model=models.student
        fields=['name','enrollment','branch']