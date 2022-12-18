from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, DeleteView, TemplateView

from .models import URL


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


class LinkRedirectView(View):
    def get(self, request, alias):
        link = get_object_or_404(URL, alias=alias)
        return redirect(f'{link.url}')


def links_404_view(request, exception=None):
    return TemplateResponse(request=request, template='url_trimmer/error_404.html', status=404)
