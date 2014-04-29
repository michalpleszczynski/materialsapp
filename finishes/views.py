from django.shortcuts import render


def finish_detail(request, finish_id, ajax_function):
    ajax_function = ajax_function.replace('{0}', finish_id)
    return render(request, 'index.html', {'ajax_function': ajax_function})