from django.contrib import admin


from goods.models import Categories, Dishes

#автоматически добвляется url 

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name','description','price','quantity','category' ]
    search_fields = ['name','description']
    list_filter = ['price','quantity','category']