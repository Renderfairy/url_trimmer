
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from . import models


def link_detail_view(request, link_id):
    link = get_object_or_404(models.SaveURL, pk=link_id)
    context = {'link': link}

    return render(request, 'url_trimmer/link_detail.html', context)


def link_redirect(request, alias):
    link = get_object_or_404(models.SaveURL, alias=alias)
    return redirect(f'{link.url}')


def link_delete(request, alias):
    link = get_object_or_404(models.SaveURL, alias=alias)
    link.delete()

    return redirect(reverse_lazy('home:home'))


def error_404(request, exception, template_name='url_trimmer/error_404.html'):
    return render(request, template_name)