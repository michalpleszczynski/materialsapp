from django.shortcuts import render

from .models import CutDetail


def cut_list(request):
    cuts = CutDetail.objects.active()
    return render(request, 'category/cut_list.html', {'cuts': cuts})