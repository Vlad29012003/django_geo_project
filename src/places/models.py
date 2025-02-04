from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.utils.text import slugify

class Place(models.Model):
    STATUS_CHOICE = [
        ('active', 'Активно'),
        ('closed', 'Закрыто'),
        ('temporary_closed', 'Временно закрыто'),
    ]

    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name="Описание")
    location = models.ForeignKey('locations.Location', on_delete=models.CASCADE, related_name='places')
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, related_name='places')
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='active')
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        verbose_name="Рейтинг",
        default=0.0
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    website = models.URLField(blank=True, verbose_name="Веб-сайт")
    email = models.EmailField(blank=True, verbose_name="Email")
    main_image = models.ImageField(upload_to='places/main/', blank=True, null=True)
    working_hours = models.JSONField(verbose_name="Часы работы", null=True, blank=True)
    price_level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Уровень цен",
        null=True,
        blank=True
    )
    features = models.JSONField(verbose_name="Особенности", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
        ordering = ['-rating', 'name']



class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='places/gallery/')
    description = models.CharField(max_length=200, blank=True)
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Изображение места"
        verbose_name_plural = "Изображения мест"
        ordering = ['-is_main', '-created_at']




























