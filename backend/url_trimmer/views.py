from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from .models import URL


def link_redirect(request, alias):
    """
        Redirect to instances original url :model:`url_trimmer.SaveURL`.

        **Context**

        ``link``
            An instance of :model:`url_trimmer.SaveURL`.

    """
    link = get_object_or_404(URL, alias=alias)
    return redirect(f'{link.url}')


def link_delete(request, alias):
    """
       Delete instance :model:`url_trimmer.SaveURL`.

       **Context**

       ``link``
           An instance of :model:`url_trimmer.SaveURL`.

   """
    link = get_object_or_404(URL, alias=alias)
    link.delete()

    return redirect(reverse_lazy('home:home'))


def error_404(request, exception, template_name='url_trimmer/error_404.html'):
    return render(request, template_name)


class LinkDetailView(LoginRequiredMixin, DetailView):
    model = URL
    context_object_name = 'link'
    template_name = 'url_trimmer/link_detail.html'
    login_url = 'users:login'


class LinkDeleteView(LoginRequiredMixin, DeleteView):
    model = URL
    pk_url_kwarg = 'alias'
    context_object_name = 'link'
    success_url = reverse_lazy('home:home')
    login_url = 'users:login'

    def get_object(self, queryset=None):
        al = self.kwargs.get('alias')
        obj = URL.objects.get(alias=al)
        if not obj.user == self.request.user:
            raise Http404
        return obj

