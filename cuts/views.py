from django.shortcuts import render

from .models import Cut


def cut_list(request):
    cuts = Cut.objects.all()
    return render(request, 'category/cut_list.html', {'cuts': cuts})