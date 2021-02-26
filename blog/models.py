from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField('Дата', default=timezone.now)
    auther = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    views = models.IntegerField('Просмотры', default=1)
    news_categories = (
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('Kivy', 'Kivy'),
        ('JavaScript', 'JavaScript'),
        ('HTML/CSS', 'HTML/CSS')
    )
    news_category = models.CharField('Рубрика', max_length=10, choices=news_categories, default='Python')
    image = models.ImageField('Обложка', default='blog/images/post-default.jpg')

    def __str__(self):
        return f'Новость № {self.id}: {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'