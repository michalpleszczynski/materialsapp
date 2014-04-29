# coding: utf-8
import json

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from .models import CutSubcategory, CutDetail


@dajaxice_register
def get_subcategories(request):
    subcategories = CutSubcategory.objects.active()
    render = render_to_string('partials/subcategory/cut_subcategory_list.html', {'subcategories': subcategories})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#cuts_link");')
    return dajax.json()


@dajaxice_register
def get_detail(request):
    detail_id = int(json.loads(request.POST.get('argv'))['detail_id'])
    detail = CutDetail.objects.get(pk=detail_id)
    render = render_to_string('partials/detail/cut_detail.html', {'detail': detail})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#cuts_link");')
    return dajax.json()