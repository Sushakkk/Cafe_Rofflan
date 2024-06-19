from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Отчество")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
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
    image = models.ImageField(upload_to='users_images',blank=True, null=True, verbose_name='Изображение')
    email = models.CharField(max_length=100,
                             validators=[
                                 RegexValidator(
                                     regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
                                     message="Введите корректный email адрес."
                                 )
                             ],
                             unique=True,
                             verbose_name="Почта"
                             )

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.surname} - Телефон: {self.phone}'
