# coding: utf-8
from __future__ import unicode_literals
import logging

import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db import connection

from . import SEARCH_TABLES
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm
from .models import Detail, Subcategory, Category


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
        html = render_to_string('partials/subcategory/subcategory-list.html', data)
        return HttpResponse(html, content_type='text/html')
    return render(request, 'partials/subcategory/subcategory-list.html', data)


def detail(request, detail_id, **data):
    detail_obj = Detail.objects.get(pk=detail_id)
    data['detail'] = detail_obj
    if request.is_ajax():
        data['base_template'] = 'ajax.html'
        html = render_to_string('partials/detail/detail.html', data)
        return HttpResponse(html, content_type='text/html')
    return render(request, 'partials/detail/detail.html', data)


@csrf_exempt
def search(request):

    def _text_search(term):
        results = []
        q_results = Detail.objects.extra(where=["name @@ plainto_tsquery('english', %s )"],
                                         params=[term]).only('id', 'name', 'type')
        for q in q_results:
            results.append({'id': q.id, 'name': q.name, 'type': q.type})
        return results

    term = request.GET.get('q', None)

    results = []
    if term and len(term) >= 3:
        # try normal search first
        results = _text_search(term)

        # if no results try fuzzy search
        if len(results) == 0:
            new_term = None
            cursor = connection.cursor()
            fuzzy_results = []
            for table in SEARCH_TABLES:
                cursor.execute(
                    """SELECT word, similarity(word, %s) AS sml
                    FROM {table_name} WHERE word %% %s and similarity(word, %s) > 0.4
                    ORDER BY sml DESC LIMIT 1;""".format(table_name=table), [term] * 3)
                row = cursor.fetchone()
                if row:
                    fuzzy_results.append(row)
            if len(fuzzy_results) > 0:
                fuzzy_results.sort(key=lambda x: x[1])
                new_term = fuzzy_results[-1][0]
            # if found some matching term, repeat normal search again with the new term
            if new_term:
                results = _text_search(new_term)
            else:
                # try to find a new term using levenshtein distance
                prev_row = None
                for table in SEARCH_TABLES:
                    cursor.execute("""SELECT word, levenshtein(%s, word) AS lev FROM {table_name}
                    where levenshtein(%s, word) < %s ORDER BY lev LIMIT 1;""".format(table_name=table),
                                   [term, term, 3 if len(term) > 4 else 2])
                    row = cursor.fetchone()
                    if row:
                        prev_row = row
                        if row[1] == 1:
                            # don't look further
                            break
                # found something with levenshtein distance of 1 or 2 from term
                if prev_row:
                    results = _text_search(prev_row[0])

    return HttpResponse(json.dumps({'ans': results}), status=200, content_type='application/json')