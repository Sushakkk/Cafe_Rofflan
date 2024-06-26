from django.contrib import admin
from baskets.admin import BasketTabAdmin
# Register your models here.
from users.models import User

# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']
    search_fields = ["username", "first_name", "last_name", "email", 'phone']

    inlines=[BasketTabAdmin,]