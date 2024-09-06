from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import *
from .models import UserInput
# Register your models here.


class OurAdminPanel(TranslatableAdmin):
    search_fields = ['translations__country__icontains']


admin.site.register(UserInput)
admin.site.register(Asia, OurAdminPanel)
admin.site.register(Europe, OurAdminPanel)
admin.site.register(License)
admin.site.register(Commond, OurAdminPanel)