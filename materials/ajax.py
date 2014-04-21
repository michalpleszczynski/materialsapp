# coding: utf-8
import json

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from .models import Material, MaterialSubcategory, MaterialDetail


@dajaxice_register
def get_materials(request):
    materials = Material.objects.active()
    render = render_to_string('partials/category/material_list.html', {'materials': materials})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#materials_link");')
    return dajax.json()


@dajaxice_register
def get_subcategories(request):
    material_id = json.loads(request.POST.get('argv'))['material_id']
    subcategories = MaterialSubcategory.objects.filter(categories=material_id)
    render = render_to_string('partials/subcategory/material_subcategory_list.html', {'subcategories': subcategories})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    return dajax.json()


@dajaxice_register
def get_detail(request):
    detail_id = json.loads(request.POST.get('argv'))['detail_id']
    detail = MaterialDetail.objects.get(pk=detail_id)
    render = render_to_string('partials/detail/material.html', {'detail': detail})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    return dajax.json()