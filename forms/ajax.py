# coding: utf-8
import json

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from .models import FormSubcategory, FormDetail


@dajaxice_register
def get_subcategories(request):
    subcategories = FormSubcategory.objects.active()
    render = render_to_string('partials/subcategory/form_subcategory_list.html', {'subcategories': subcategories})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#forms_link");')
    return dajax.json()


@dajaxice_register
def get_detail(request):
    detail_id = int(json.loads(request.POST.get('argv'))['detail_id'])
    detail = FormDetail.objects.get(pk=detail_id)
    render = render_to_string('partials/detail/form_detail.html', {'detail': detail})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#forms_link");')
    return dajax.json()