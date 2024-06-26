from django.contrib import admin

# Register your models here.
from baskets.models import Baskets

# admin.site.register(Baskets)
class BasketTabAdmin(admin.TabularInline):
    model = Baskets
    fields = ['dish', 'quantity', 'created_timestamp']
    list_display = ['user', 'dish', 'quantity', 'created_timestamp']
    search_fields = ['user', 'dish',  'created_timestamp']
    readonly_fields =('created_timestamp',)
    extra =1

@admin.register(Baskets)
class BasketsAdmin(admin.ModelAdmin):
    list_display = ['user', 'dish', 'quantity', 'created_timestamp']
    search_fields = ['user', 'dish',  'created_timestamp']
    list_filter = ['user', 'dish', 'quantity', 'created_timestamp']

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"