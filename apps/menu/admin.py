from django.contrib import admin

from apps.menu.models import Ingredient, Dish, Menu


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


class DishAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'get_ingredients',
    )


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'dish',
        'category',
        'portion',
    )


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Menu, MenuAdmin)
