from django.db import models

from apps.users.models import User


CATEGORY_CHOICES = (
        ('BREAKFAST', 'Breakfast'),
        ('LUNCH', 'Lunch'),
        ('DINNER', 'Dinner'),
    )


class Ingredient(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    ingredients = models.ManyToManyField(Ingredient, related_name='dishes')

    def get_ingredients(self):
        return ",".join([str(p) for p in self.ingredients.all()])

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name


class Menu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    category = models.CharField(max_length=150, choices=CATEGORY_CHOICES)
    portion = models.IntegerField()

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return f'{self.user.email} {self.dish.name} {self.category}'
