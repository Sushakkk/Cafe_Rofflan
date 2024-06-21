from django.db import models
from users.models import User
from goods.models import Dishes 
from django.core.validators import RegexValidator

# class Order_dishQuerryset(models.QuerySet):
#     def total_price(self):
#         return sum(baskets.produts_price() for baskets in self)
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name='Пользователь', default=None)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    phone_number = models.CharField(max_length=20,
                             validators=[
                                 RegexValidator(
                                     regex=r'^\+7 \(\d{3}\)-\d{3}-\d{4}$',
                                     message="Номер телефона должен быть в формате +7 (000)-000-0000"
                                 )
                             ],
                             unique=True,
                             verbose_name='Телефон'
                             )
    requires_delivery = models.BooleanField(default=False,verbose_name='Требуется доставка') 
    delivery_address = models.TextField(null=True, blank=True, verbose_name='Адрес доставки')
    payment_on_get = models.BooleanField(default=False, verbose_name='Оплата при получении')
    is_paid = models.BooleanField(default=False,verbose_name='Оплачено')
    status = models.CharField(max_length=50,default='В разработке', verbose_name='Статус заказа')

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.first_name} {self.user.last_name}"
    

class Order_dish(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Заказ')
    dish = models.ForeignKey(to=Dishes, on_delete=models.SET_DEFAULT, null=True, verbose_name='Блюдо', default=None)
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.DecimalField(default=0.00, max_digits=7,decimal_places=2,verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0,verbose_name='Количество')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')
    
    class Meta:
        db_table = 'order_dish'
        verbose_name = 'Заказ блюда'
        verbose_name_plural = 'Заказы блюд'

    # objects: Manager[Self] = Order_dishQueryset.as_manager()
    #     def get_queryset(self):
    #         return super().get_queryset().filter()
    
    def __str__(self):
        return round(self.price * self.quantity, 2)
    
    def __str__(self):
        return f"Товар {self.name} | Заказ № {self.order.pk}"
    
    
    