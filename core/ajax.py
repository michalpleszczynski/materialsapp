# coding: utf-8
from __future__ import unicode_literals
import json
import logging

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from sorl.thumbnail.shortcuts import get_thumbnail

from .models import Image


logger = logging.getLogger(__name__)


def page_change_routine(dajax, render, active_link):
    dajax.assign('#content', 'innerHTML', render)
    if not active_link.startswith('#'):
        active_link = '#' + active_link
    dajax.script('setActiveLink("' + active_link + '");')
    dajax.remove_css_class('#bottom-box', 'transparent')


@dajaxice_register
def get_image(request, id):
    dajax = Dajax()
    try:
        image = Image.objects.only('image').get(pk=int(id)).image
        mini = get_thumbnail(image, 'x80', upscale=False)
        output = ('<a style="width:%spx;display:block;margin:0 0 10px" class="thumbnail" target="_blank" href="%s">'
                  '<img src="%s"></a>' % (mini.width, image.url, mini.url))
        dajax.assign('#admin_related_image', 'innerHTML', output)
    except Exception as e:
        print("Unable to get the thumbnail", e)
    return dajax.json()