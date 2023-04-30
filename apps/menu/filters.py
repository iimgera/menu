import django_filters
from apps.menu.models import Dish


class DishFilter(django_filters.FilterSet):
    ingredients = django_filters.CharFilter(
        field_name='ingredients__name', lookup_expr='iexact', )

    def filter_ingredients(self, queryset, name, value):
        ingredients = value.split(',')
        return ingredients.filter(
            ingredients__name__iexact=ingredients).distinct()

    class Meta:
        model = Dish
        fields = ['name', 'ingredients']
