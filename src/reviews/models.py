from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator , MaxValueValidator

class Review(models.Model):
    place = models.ForeignKey('places.Place', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Оценка"
    )
    title = models.CharField(max_length=255, verbose_name="Заголовок", blank=True)
    comment = models.TextField(verbose_name="Комментарий")
    visit_date = models.DateField(verbose_name="Дата посещения", null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_reviews', blank=True)
    is_verified = models.BooleanField(default=False, verbose_name="Проверенный отзыв")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Отзыв от {self.user.username} j {self.place.name}'
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        unique_together = ['place', 'user']
        ordering = ['-created_at']



class ReviewImage(models.Model):
    review = models.ForeignKey(Review,on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='reviews/images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Изображение к отзыву"
        verbose_name_plural = "Изображения к отзывам"













