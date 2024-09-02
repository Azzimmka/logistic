from django.db import models
from django.utils.translation import gettext_lazy as _


class Asia(models.Model):
    country = models.CharField(_('country'), max_length=50)
    logo = models.ImageField()
    discription = models.TextField(_('discription'))

    created = models.DateTimeField(auto_now_add=True, null=True, )

    

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.country
    
    class Meta:
        verbose_name = 'Добавить Азиатскую'
        verbose_name_plural = 'Страны Азии'
    
class Europe(models.Model):
    country = models.CharField(_('country'), max_length=50)
    logo = models.ImageField()
    discription = models.TextField(_('discription'))

    def __str__(self):
        return self.country
    
    class Meta:
        verbose_name = 'Добавить Европейскую'
        verbose_name_plural = 'Страны Европы'



class License(models.Model):
    name = models.CharField(max_length=255)  # Имя лицензии
    pdf = models.FileField(upload_to='licenses/', null=True, blank=True)  # Поле для загрузки PDF файла

    def __str__(self):
        return self.name
