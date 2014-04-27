# coding: utf-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from .models import FormSubcategory


@dajaxice_register
def get_subcategories(request):
    subcategories = FormSubcategory.objects.active()
    render = render_to_string('partials/subcategory/form_subcategory_list.html', {'subcategories': subcategories})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#forms_link");')
    return dajax.json()