
from django.shortcuts import render, redirect, get_object_or_404

from . import models


def link_detail_view(request, link_id):
    link = get_object_or_404(models.SaveURL, pk=link_id)
    context = {'link': link}

    return render(request, 'url_trimmer/link_detail.html', context)


def link_redirect(request, alias):
    link = get_object_or_404(models.SaveURL, alias=alias)
    return redirect(f'{link.url}')