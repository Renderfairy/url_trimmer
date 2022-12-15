from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from django.views.generic.edit import FormMixin

from url_trimmer import forms, models


def home_view(request):
    """
        Display form :form: `url_trimmer.AddURL` and list of instances :model: `url_trimmer.SaveURL`.

        **Context**
        ``form``
            An instance of :form: `url_trimmer.AddURL`

        ``links``
            An instance of :model: `url_trimmer.SaveURL`.

        **Template:**
        Includes :template: `url_trimmer/add_url.html` and :template: `url_trimmer/links_list.html`
        :template:`home/home.html`

        """
    if request.user.is_authenticated:
        form = forms.AddUrl(request.POST or None)
        links = models.URL.objects.filter(user=request.user)
        context = {
            'form': form,
            'links': links,
        }

        if request.method == 'POST':
            if form.is_valid():
                url = form.save(commit=False)
                url.user = request.user
                url.save()
                return HttpResponseRedirect(reverse_lazy('home:home'))

        return render(request, 'home/home.html', context)

    return redirect(reverse_lazy('users:login'))


class HomeView(LoginRequiredMixin, FormMixin, ListView):
    template_name = 'home/home.html'
    model = models.URL
    form_class = forms.AddUrl
    login_url = 'users:login'
    success_url = reverse_lazy('home:home_2')

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