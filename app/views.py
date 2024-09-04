from django.shortcuts import render, redirect
from .models import Asia, Europe, License
from django.http import Http404
from .forms import UserInputForm

# Create your views here.


def base(request):
    country = Asia.objects.all()
    countries = Europe.objects.all()
    
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')  # перенаправляем на страницу успешной отправки
    else:
        form = UserInputForm()

    context = {
        'country': country,
        'countries': countries,
        'form': form,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')


def some(request):
    return render(request, 'some.html')

def contacts(request):
    return render(request, 'contacts.html')


def license_view(request):
    license = License.objects.first()
    if not license:
        raise Http404("License not found")
    return render(request, 'license.html', {'license': license})

def services(request):
    country = Asia.objects.all()
    countries = Europe.objects.all()
    context = {
        'country': country,
        'countries': countries,
    }
    return render(request, 'services.html', context)




def user_input_view(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')  # перенаправляем на страницу успешной отправки
    else:
        form = UserInputForm()

    return render(request, 'about.html', {'form': form})