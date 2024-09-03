from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import *
# Register your models here.


class OurAdminPanel(TranslatableAdmin):
    search_fields = ['translations__country__icontains']


admin.site.register(Asia, OurAdminPanel)
admin.site.register(Europe, OurAdminPanel)
admin.site.register(License)