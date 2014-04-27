from django.shortcuts import render

from .models import Material, MaterialDetail


def material_list(request, ajax_function):
    return render(request, 'index.html', {'ajax_function': ajax_function})


def material_subcategories(request, material_id, ajax_function):
    ajax_function = ajax_function.replace('{0}', material_id)
    return render(request, 'index.html', {'ajax_function': ajax_function})


def material_detail(request, id):
    material = MaterialDetail.objects.active().get(pk=id)
    return render(request, 'detail/detail.html', {'detail': material})
