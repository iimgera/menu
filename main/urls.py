from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.users.views import RegistrUserView, AuthView, UserDetailListView
from apps.menu.views import (
    IngredientListCreateView,
    IngredientRetrieveUpdateDestroyView,
    DishListCreateView,
    DishRetrieveUpdateDestroyView,
    MenuListCreateView,
    MenuRetrieveUpdateDestroyView,
)


schema_view = get_schema_view(
    openapi.Info(
        title="Menu API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


api_v1 = [
    path('api-auth', include('rest_framework.urls')),
    path('auth/', AuthView.as_view()),
    path('registr/', RegistrUserView.as_view(), name='registr'),
    path('users/', UserDetailListView.as_view(), name='user-detail'),

    path('ingredients/', IngredientListCreateView.as_view(), name='ingredient_list_create'),
    path('ingredients/<int:pk>/', IngredientRetrieveUpdateDestroyView.as_view(), name='ingredient_detail'),
    path('dishes/', DishListCreateView.as_view(), name='dish_list_create'),
    path('dishes/filter/', DishListCreateView.as_view(), name='dish-filter'),
    path('dishes/<int:pk>/', DishRetrieveUpdateDestroyView.as_view(), name='dish_detail'),
    path('menus/', MenuListCreateView.as_view(), name='menu_list_create'),
    path('menus/<int:pk>/', MenuRetrieveUpdateDestroyView.as_view(), name='menu_detail'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
    path('api/v1/', include(api_v1)),
]
