# coding: utf-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from .models import FinishSubcategory


@dajaxice_register
def get_finishes(request):
    finishes = FinishSubcategory.objects.active()
    render = render_to_string('partials/finish_list.html', {'finishes': finishes})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#finishes_link");')
    return dajax.json()