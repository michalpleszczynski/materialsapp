from django.shortcuts import render

from .models import FinishDetail


def finish_list(request):
    finishes = FinishDetail.objects.active()
    return render(request, 'category/finish_subcategory_list.html', {'finishes': finishes})