# coding: utf-8
import logging

from django.forms import Select
from django.forms.util import flatatt
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from sorl.thumbnail.shortcuts import get_thumbnail

from .models import Image

logger = logging.getLogger(__name__)


class AdminRelatedImageWidget(Select):

    def render(self, name, value, attrs=None, choices=()):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html('<select{0} onchange="get_image(this.value);">', flatatt(final_attrs))]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append('</select>')
        output = '\n'.join(output)
        try:
            image = Image.objects.only('image').get(id=value).image
            mini = get_thumbnail(image, 'x80', upscale=False)
        except Exception as e:
            logger.warning("Unable to get the thumbnail", exc_info=e)
        else:
            output = ('<div style="float:left;margin-right:5px;">%s<div id="admin_related_image">'
                      '<a style="width:%spx;display:block;margin:0 0 10px" class="thumbnail" target="_blank" href="%s">'
                      '<img src="%s"></a></div></div>') % (output, mini.width, image.url, mini.url)
        return mark_safe(output)