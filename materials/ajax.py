# coding: utf-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.template.loader import render_to_string

from .models import Material


@dajaxice_register
def get_materials(request):
    materials = Material.objects.active()
    render = render_to_string('partials/material_list.html', {'materials': materials})

    dajax = Dajax()
    dajax.assign('#content', 'innerHTML', render)
    dajax.script('set_active_link("#materials_link");')
    return dajax.json()