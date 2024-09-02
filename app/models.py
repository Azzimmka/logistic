from django.db import models



class Asia(models.Model):
    country = models.CharField(max_length=50)
    logo = models.ImageField()
    discription = models.TextField()

    def __str__(self):
        return self.country
    
    class Meta:
        verbose_name = 'Добавить Азиатскую'
        verbose_name_plural = 'Страны Азии'
    
class Europe(models.Model):
    country = models.CharField(max_length=50)
    logo = models.ImageField()
    discription = models.TextField()

    def __str__(self):
        return self.country
    
    class Meta:
        verbose_name = 'Добавить Европейскую'
        verbose_name_plural = 'Страны Европы'
