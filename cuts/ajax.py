# coding: utf-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from core.ajax import page_change_routine
from .models import CutSubcategory, CutDetail


@dajaxice_register
def get_subcategories(request):
    subcategories = CutSubcategory.objects.active()
    render = render_to_string('partials/subcategory/cut_subcategory_list.html', {'subcategories': subcategories})

    dajax = Dajax()
    page_change_routine(dajax, render, 'cuts_link')
    return dajax.json()


@dajaxice_register
def get_detail(request, detail_id):
    detail = CutDetail.objects.get(pk=int(detail_id))
    render = render_to_string('partials/detail/cut_detail.html', {'detail': detail})

    dajax = Dajax()
    page_change_routine(dajax, render, 'cuts_link')
    return dajax.json()