from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from apps.menu.filters import DishFilter
from apps.menu.models import Dish, Ingredient, Menu
from apps.menu.serializers import (
    DishSerializer,
    IngredientSerializer,
    MenuSerializer,
)


class IngredientListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAdminUser]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class DishListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DishFilter
    filterset_fields = ['ingredients', ]


class DishRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class MenuListCreateView(generics.ListCreateAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Menu.objects.all()
        else:
            return Menu.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MenuRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Menu.objects.all()
        else:
            return Menu.objects.filter(user=user)
