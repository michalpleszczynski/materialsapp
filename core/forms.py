# coding: utf-8
from django import forms

from .models import Subcategory


class SubcategoryForm(forms.ModelForm):

    class Meta:
        model = Subcategory
        widgets = {
            'caption': forms.Textarea(),
        }


class DetailForm(forms.ModelForm):

    class Meta:
        model = Subcategory
        widgets = {
            'caption': forms.Textarea(),
            'facts': forms.Textarea(),
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=15, required=True, label="",
                           widget=forms.TextInput(attrs={'placeholder': 'Your name:'}))
    email = forms.EmailField(required=True, label="",
                             widget=forms.EmailInput(attrs={'placeholder': 'Your email:'}))
    message = forms.CharField(max_length=250, label="",
                              widget=forms.Textarea(attrs={'placeholder': 'Your message:'}))