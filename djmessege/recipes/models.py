from django.db import models
from django.conf import settings
from django.db.models import Avg

class Article(models.Model):
    title = models.CharField('Назва рецепту', max_length=100)
    photo = models.ImageField('Фотографія рецепту', upload_to='recipe_photos/', blank=True, null=True)
    description = models.TextField('Короткий опис' ,blank=True)
    ingredients = models.TextField('Інгредієнти', blank=True)
    instructions = models.JSONField('Інструкції', default=list,)  # Можна зберігати кроки у форматі JSON
    notes = models.TextField('Примітки', blank=False)
    created_at = models.DateTimeField('Дата створення', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/recipes/{self.id}'

    def average_rating(self):
        rating = self.ratings.aggregate(Avg('rating'))['rating__avg']
        return round(rating, 1) if rating else '0'


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)])

    class Meta:
        unique_together = ('user', 'article')

    def __str__(self):
        return f'{self.user.username} rated {self.article.title} {self.rating} stars'
