from django.shortcuts import render

from .models import FormDetail


def form_list(request):
    forms = FormDetail.objects.active()
    return render(request, 'category/form_subcategory_list.html', {'forms': forms})