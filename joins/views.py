from django.shortcuts import render

from .models import JoinSubcategory


def join_list(request):
    joins = JoinSubcategory.objects.active()
    return render(request, 'category/join_list.html', {'joins': joins})