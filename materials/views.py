from django.shortcuts import render

from .models import Material, MaterialDetail


def material_list(request, ajax_function):
    return render(request, 'index.html', {'ajax_function': ajax_function})


def material_ajax_content(request, material_id, ajax_function):
    ajax_function = ajax_function.replace('{0}', material_id)
    return render(request, 'index.html', {'ajax_function': ajax_function})
