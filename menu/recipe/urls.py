from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
]