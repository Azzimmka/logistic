from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import *
# Register your models here.

admin.site.register(Asia, TranslatableAdmin)
admin.site.register(Europe, TranslatableAdmin)
admin.site.register(License)