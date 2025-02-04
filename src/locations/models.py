from django.db import models
from django.contrib.gis.db import models
from django.utils.text import slugify

class Location(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название места")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    point = models.PointField(verbose_name="Координаты")
    address = models.CharField(max_length=255, verbose_name="Адрес", blank=True)
    city = models.CharField(max_length=100, verbose_name="Город")
    region = models.CharField(max_length=100, verbose_name="Регион", blank=True)
    postal_code = models.CharField(max_length=10, verbose_name="Почтовый индекс", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self,  *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.city}"
    

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
        ordering = ['city', 'name']





