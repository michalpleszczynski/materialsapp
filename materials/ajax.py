# coding: utf-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from core.ajax import page_change_routine
from .models import Material, MaterialSubcategory, MaterialDetail


@dajaxice_register
def get_materials(request):
    materials = Material.objects.active()
    render = render_to_string('partials/category/material_list.html', {'materials': materials})

    dajax = Dajax()
    page_change_routine(dajax, render, 'materials_link')
    return dajax.json()


@dajaxice_register
def get_subcategories(request, material_id):
    subcategories = MaterialSubcategory.objects.filter(categories=int(material_id))
    render = render_to_string('partials/subcategory/material_subcategory_list.html',
                              {'subcategories': subcategories, 'material_id': material_id})

    dajax = Dajax()
    page_change_routine(dajax, render, 'materials_link')
    return dajax.json()


@dajaxice_register
def get_detail(request, detail_id):
    detail = MaterialDetail.objects.get(pk=int(detail_id))
    render = render_to_string('partials/detail/material_detail.html', {'detail': detail})

    dajax = Dajax()
    page_change_routine(dajax, render, 'materials_link')
    return dajax.json()