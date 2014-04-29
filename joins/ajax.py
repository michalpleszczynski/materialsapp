# coding: utf-8
import json

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from .models import JoinSubcategory, JoinDetail


@dajaxice_register
def get_subcategories(request):
    subcategories = JoinSubcategory.objects.active()
    render = render_to_string('partials/subcategory/join_subcategory_list.html', {'subcategories': subcategories})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#joins_link");')
    return dajax.json()


@dajaxice_register
def get_detail(request):
    detail_id = int(json.loads(request.POST.get('argv'))['detail_id'])
    detail = JoinDetail.objects.get(pk=detail_id)
    render = render_to_string('partials/detail/join_detail.html', {'detail': detail})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#joins_link");')
    return dajax.json()