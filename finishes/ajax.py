# coding: utf-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from .models import FinishDetail


@dajaxice_register
def get_finishes(request):
    finishes = FinishDetail.objects.active()
    render = render_to_string('partials/subcategory/finish_list.html', {'finishes': finishes})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#finishes_link");')
    return dajax.json()