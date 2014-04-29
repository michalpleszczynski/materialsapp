# coding: utf-8
from django.shortcuts import render


def cut_detail(request, cut_id, ajax_function):
    ajax_function = ajax_function.replace('{0}', cut_id)
    return render(request, 'index.html', {'ajax_function': ajax_function})