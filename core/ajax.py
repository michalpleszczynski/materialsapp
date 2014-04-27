# coding: utf-8
import json
import logging

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from sorl.thumbnail.shortcuts import get_thumbnail

from .models import Image


logger = logging.getLogger(__name__)


@dajaxice_register
def get_image(request):
    dajax = Dajax()
    try:
        image_id = int(json.loads(request.POST.get('argv'))['id'])
        image = Image.objects.only('image').get(pk=image_id).image
        mini = get_thumbnail(image, 'x80', upscale=False)
        output = ('<a style="width:%spx;display:block;margin:0 0 10px" class="thumbnail" target="_blank" href="%s">'
                  '<img src="%s"></a>' % (mini.width, image.url, mini.url))
        dajax.assign('#admin_related_image', 'innerHTML', output)
    except Exception as e:
        print("Unable to get the thumbnail", e)
    return dajax.json()