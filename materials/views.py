from django.shortcuts import render

from .models import Material, MaterialSubcategory


def material_list(request):
    materials = Material.objects.all()
    return render(request, 'category/material_list.html', {'materials': materials})


def material_detail(request, id):
    material = MaterialSubcategory.objects.get(pk=id)
    return render(request, 'subcategory/materials/material_detail.html', {'material': material})
