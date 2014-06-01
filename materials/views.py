# coding: utf-8
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Material, MaterialSubcategory, MaterialDetail


ACTIVE_LINK = '#materials_link'


def material_list(request):
    categories = Material.objects.active()
    data = {'categories': categories, 'active_link': ACTIVE_LINK, 'base_template': 'base.html'}
    if request.is_ajax():
        data['base_template'] = 'ajax.html'
        html = render_to_string('partials/category/material_list.html', data)
        return HttpResponse(html, content_type='text/html')
    return render(request, 'partials/category/material_list.html', data)


def material_subcategory(request, category_id):
    subcategories = MaterialSubcategory.objects.filter(categories=category_id)
    data = {'subcategories': subcategories, 'category_id': category_id,
            'detail_url': 'material_detail', 'active_link': ACTIVE_LINK, 'base_template': 'base.html'}
    if request.is_ajax():
        data['base_template'] = 'ajax.html'
        html = render_to_string('partials/subcategory/subcategory_list.html', data)
        return HttpResponse(html, content_type='text/html')
    return render(request, 'partials/subcategory/subcategory_list.html', data)


def material_detail(request, material_id):
    detail = MaterialDetail.objects.get(pk=material_id)
    data = {'detail': detail, 'active_link': ACTIVE_LINK, 'base_template': 'base.html'}
    if request.is_ajax():
        data['base_template'] = 'ajax.html'
        html = render_to_string('partials/detail/detail.html', data)
        return HttpResponse(html, content_type='text/html')
    return render(request, 'partials/detail/detail.html', data)
