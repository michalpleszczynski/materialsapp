from django.shortcuts import render

from .models import Join


def join_list(request):
    joins = Join.objects.all()
    return render(request, 'category/join_list.html', {'joins': joins})