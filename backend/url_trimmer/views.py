
from django.shortcuts import render, redirect, get_object_or_404

from . import forms, models


def link_detail_view(request, link_id):
    link = get_object_or_404(models.SaveURL, pk=link_id)
    context = {'link': link}

    return render(request, 'url_trimmer/link_detail.html', context)

