from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class Asia(TranslatableModel):
    translations = TranslatedFields(
        country = models.CharField(_('country'), max_length=50),
        description = models.TextField(_('description'))
    )
    logo = models.ImageField(upload_to='asia_logos/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Asian Country')
        verbose_name_plural = _('Asian Countries')

    def __str__(self):
        return self.country

class Europe(TranslatableModel):
    translations = TranslatedFields(
        country = models.CharField(_('country'), max_length=50),
        description = models.TextField(_('description'))
    )
    logo = models.ImageField(upload_to='europe_logos/', null=True, blank=True)

    class Meta:
        verbose_name = _('European Country')
        verbose_name_plural = _('European Countries')

    def __str__(self):
        return self.country

class License(models.Model):
    name = models.CharField(max_length=255)  # Имя лицензии
    pdf = models.FileField(upload_to='licenses/', null=True, blank=True)  # Поле для загрузки PDF файла

    def __str__(self):
        return self.name


class UserInput(models.Model):
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    information = models.TextField(verbose_name='Информация')

    def __str__(self):
        return f'{self.phone_number} - {self.information}'