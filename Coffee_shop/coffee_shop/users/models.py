

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    phone = models.CharField(max_length=20,
                             validators=[
                                 RegexValidator(
                                     regex=r'^\+7 \(\d{3}\)-\d{3}-\d{4}$',
                                     message="Номер телефона должен быть в формате +7 (000)-000-0000"
                                 )
                             ],
                             unique=True,
                             verbose_name='Телефон'
                             )

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
        # return f'{self.first_name} {self.last_name} - Телефон: {self.phone}'
