from django.shortcuts import render

from .models import FormSubcategory


def form_list(request):
    forms = FormSubcategory.objects.active()
    return render(request, 'category/form_list.html', {'forms': forms})