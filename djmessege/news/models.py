from django.db import models

class Article(models.Model):
    title = models.CharField('Назва',max_length=50)
    intro = models.CharField('Анонс',max_length=50)
    full_text = models.TextField('Текст')
    date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  f'/news/{self.id}'