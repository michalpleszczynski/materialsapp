from django.shortcuts import render

from .models import CutSubcategory


def cut_list(request):
    cuts = CutSubcategory.objects.active()
    return render(request, 'category/cut_list.html', {'cuts': cuts})