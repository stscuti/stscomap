from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def descargas(request):
    media = '/media/'
    return render(request, 'descargas.html', {
        'ruta': media
    })

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {
        'form': form
    })

@login_required
def secret_page(request):
    return render(request, 'base_juan.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'base_juan.html'