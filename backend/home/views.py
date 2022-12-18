from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from django.views.generic.edit import FormMixin

from url_trimmer import forms, models


class HomeView(LoginRequiredMixin, FormMixin, ListView):
    template_name = 'home/home.html'
    model = models.URL
    form_class = forms.AddUrl
    login_url = 'users:login'
    success_url = reverse_lazy('home:home')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            url = form.save(commit=False)
            url.user = request.user
            url.save()
            return self.form_valid(form)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = self.get_queryset()
        return context

    def get_queryset(self):
        return models.URL.objects.filter(user=self.request.user)