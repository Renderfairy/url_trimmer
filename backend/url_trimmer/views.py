from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from . import forms


def add_new_url(request):
    form = forms.AddUrl(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            url = form.save(commit=False)
            url.user = request.user
            url.save()
            return HttpResponseRedirect(reverse_lazy('home:home'))

    return render(request, 'url_trimmer/add_url.html', {'form': form})
