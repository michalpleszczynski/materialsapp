import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import ContactForm
from .models import Detail


logger = logging.getLogger(__name__)


def home(request):
    blog_posts = {
        'posts': [
            {
                'title': 'Lorem ipsum dolore...',
                'text': """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus consectetur nunc
            fermentum gravida congue. Pellentesque habitant morbi tristique senectus et netus et malesuada
            fames ac turpis egestas. Duis bibendum, massa quis varius pretium, erat velit volutpat ligula,
            eget interdum urna nisl ac tellus.""",
                'date': '5:37 PM, 04-05-2014',
            },
            {
                'title': 'Nunc in congue eros. Integer fermentum vulputate...',
                'text': """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus consectetur nunc
            fermentum gravida congue. Pellentesque habitant morbi tristique senectus et netus et malesuada
            fames ac turpis egestas. Duis bibendum, massa quis varius pretium, erat velit volutpat ligula,
            eget interdum urna nisl ac tellus.""",
                'date': '10:02 AM, 02-02-2014',
            },
            {
                'title': 'Fusce tempor nulla ac hendrerit rutrum.',
                'text': """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus consectetur nunc
            fermentum gravida congue. Pellentesque habitant morbi tristique senectus et netus et malesuada
            fames ac turpis egestas. Duis bibendum, massa quis varius pretium, erat velit volutpat ligula,
            eget interdum urna nisl ac tellus.""",
                'date': '8:52 PM, 08-01-2013',
            },
        ],
    }
    images = ['images/no_image.png'] * 9
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            logger.debug('Sending email.')
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ContactForm()
    data = {'posts': blog_posts['posts'], 'form': form, 'gallery': images, 'base_template': 'base.html'}
    if request.is_ajax():
        data['base_template'] = 'ajax.html'
        html = render_to_string('index.html', data)
        return HttpResponse(html, 'text/html')
    return render(request, 'index.html', data)


def subcategory(request, **data):
    if request.is_ajax():
        data['base_template'] = 'ajax.html'
        html = render_to_string('partials/subcategory/subcategory_list.html', data)
        return HttpResponse(html, content_type='text/html')
    return render(request, 'partials/subcategory/subcategory_list.html', data)


def detail(request, detail_id, **data):
    detail_obj = Detail.objects.get(pk=detail_id)
    data['detail'] = detail_obj
    if request.is_ajax():
        data['base_template'] = 'ajax.html'
        html = render_to_string('partials/detail/detail.html', data)
        return HttpResponse(html, content_type='text/html')
    return render(request, 'partials/detail/detail.html', data)