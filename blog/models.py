from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField('Дата', default=timezone.now)
    auther = models.ForeignKey(User, verbose_name='Автор',
                               on_delete=models.CASCADE)
    views = models.IntegerField('Просмотры', default=1)
    news_categories = (
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('Kivy', 'Kivy'),
        ('JavaScript', 'JavaScript'),
        ('HTML/CSS', 'HTML/CSS')
    )
    news_category = models.CharField('Рубрика', max_length=10,
                                     choices=news_categories, default='Python')
    image = models.ImageField('Обложка', default='blog/images/post-default.jpg')

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return f'Новость: {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Message(models.Model):
    # Каждое сообщение будет содержать поля:
    # тема, текст сообщения, почта отправителя и дата
    subject = models.CharField(max_length=250)
    email = models.EmailField(max_length=100, default="")
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject
    #
    # class Meta:
    #     verbose_name = 'Сообщение'
    #     verbose_name_plural = 'Сообщения'