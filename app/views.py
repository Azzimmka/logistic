from django.shortcuts import render
from .models import Asia, Europe
from django.utils.translation import gettext as _
# Create your views here.


def base(request):
    country = Asia.objects.all()
    countries = Europe.objects.all()
    context = {
        'country': country,
        'countries': countries,
        'hello': _('Hello Azza')
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
