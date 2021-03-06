from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

GENDER_CHOICES = (('male', 'Мужчина'),('famale', 'Женщина'),)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    img = models.ImageField('Фото пользователя', default='avatar_default.png', upload_to='user_images')
    telephone = models.CharField('Телефон', max_length=300, default='00000000000')
    gender = models.CharField('Пол', max_length=40, choices=GENDER_CHOICES, default='Мужчина')
    agreement = models.BooleanField('Согласие на отправку писем', default=True)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'профайл'
        verbose_name_plural = 'профайлы'