from django.db import models
from users.models import User
from goods.models import Dishes


# Create your models here.

class BasketQuerySet(models.QuerySet):
    def total_price(self) -> int:
        return sum(Baskets.dish_price() for basket in self)

    def total_quantity(self):
        if self:
            return sum(Baskets.quantity for basket in self)

        return 0


class Baskets(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    dish = models.ForeignKey(to=Dishes, on_delete=models.CASCADE, verbose_name='Блюдо')
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        db_table = 'basket'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"
        ordering = ("id",)

    def dishes_price(self):
        return round(self.dish.sell_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Корзина: {self.user.first_name} {self.user.last_name} {self.user.username}  | Товар {self.dish.name} | Количество: {self.quantity}'

        return f'Анонимная корзина | Товар {self.dish.name} | Количество {self.quantity}'
