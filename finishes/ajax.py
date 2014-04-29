# coding: utf-8
import json

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from .models import FinishSubcategory, FinishDetail


@dajaxice_register
def get_subcategories(request):
    subcategories = FinishSubcategory.objects.active()
    render = render_to_string('partials/subcategory/finish_subcategory_list.html', {'subcategories': subcategories})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#finishes_link");')
    return dajax.json()


@dajaxice_register
def get_detail(request):
    detail_id = int(json.loads(request.POST.get('argv'))['detail_id'])
    detail = FinishDetail.objects.get(pk=detail_id)
    render = render_to_string('partials/detail/finish_detail.html', {'detail': detail})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#finishes_link");')
    return dajax.json()