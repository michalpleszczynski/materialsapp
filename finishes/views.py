from django.shortcuts import render

from .models import FinishSubcategory


def finish_list(request):
    finishes = FinishSubcategory.objects.active()
    return render(request, 'category/finish_list.html', {'finishes': finishes})