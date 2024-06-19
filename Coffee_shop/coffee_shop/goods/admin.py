from django.contrib import admin


from goods.models import Categories, Dishes

#автоматически добвляется url 

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}