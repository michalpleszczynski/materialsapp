from django.shortcuts import render

from .models import Form


def form_list(request):
    forms = Form.objects.all()
    return render(request, 'category/form_list.html', {'forms': forms})