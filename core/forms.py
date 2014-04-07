# coding: utf-8
from django import forms

from .models import Subcategory


class SubcategoryForm(forms.ModelForm):

    class Meta:
        model = Subcategory
        widgets = {
            'caption': forms.Textarea(),
            'facts': forms.Textarea(),
        }