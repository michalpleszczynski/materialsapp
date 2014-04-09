from django.shortcuts import render

from .models import Finish


def finish_list(request):
    finishes = Finish.objects.all()
    return render(request, 'category/finish_list.html', {'finishes': finishes})