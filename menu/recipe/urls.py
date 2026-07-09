from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('edit-recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('delete-recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
]