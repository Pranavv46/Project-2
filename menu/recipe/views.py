from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {
        'name': 'Pranav'
    })

from .models import Recipe
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {
        'recipes': recipes
    })

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', {
        'recipe': recipe
    }) 