from django.shortcuts import render


def form_detail(request, form_id, ajax_function):
    ajax_function = ajax_function.replace('{0}', form_id)
    return render(request, 'index.html', {'ajax_function': ajax_function})