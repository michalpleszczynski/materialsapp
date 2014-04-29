from django.shortcuts import render

from .models import JoinDetail


def join_detail(request, join_id, ajax_function):
    ajax_function = ajax_function.replace('{0}', join_id)
    return render(request, 'index.html', {'ajax_function': ajax_function})