from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy


from url_trimmer import forms, models


def home_view(request):
    if request.user.is_authenticated:
        form = forms.AddUrl(request.POST or None)
        links = models.SaveURL.objects.filter(user=request.user)
        context = {
            'form': form,
            'path': request.path,
            'links': links,
        }

        if request.method == 'POST':
            if form.is_valid():
                url = form.save(commit=False)
                url.user = request.user
                url.alias = models.SaveURL.objects.all().count()
                url.save()
                return HttpResponseRedirect(reverse_lazy('home:home'))

        return render(request, 'home/home.html', context)

    return render(request, 'home/home.html')
