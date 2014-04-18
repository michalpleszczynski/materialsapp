# coding: utf-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from .models import FormDetail


@dajaxice_register
def get_forms(request):
    forms = FormDetail.objects.active()
    render = render_to_string('partials/form_list.html', {'forms': forms})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#forms_link");')
    return dajax.json()