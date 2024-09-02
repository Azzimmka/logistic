from django.shortcuts import render
from .models import Asia, Europe
# Create your views here.


def base(request):
    country = Asia.objects.all()
    countries = Europe.objects.all()
    context = {
        'country': country,
        'countries': countries,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

from django.shortcuts import render
from .models import License

from django.http import Http404

def license_view(request):
    license = License.objects.first()
    if not license:
        raise Http404("License not found")
    return render(request, 'license.html', {'license': license})
