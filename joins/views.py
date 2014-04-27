from django.shortcuts import render

from .models import JoinDetail


def join_list(request):
    joins = JoinDetail.objects.active()
    return render(request, 'category/join_subcategory_list.html', {'joins': joins})