from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SkyUserCreationForm


def register(request):
    if request.method == 'POST':
        form = SkyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = SkyUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
