from django.shortcuts import render

from .models import Material, MaterialDetail


def material_list(request):
    materials = Material.objects.active()
    return render(request, 'category/material_list.html', {'materials': materials})


def material_detail(request, id):
    material = MaterialDetail.objects.active().get(pk=id)
    return render(request, 'subcategory/materials/material_detail.html', {'material': material})
