from django.shortcuts import render, redirect
from .models import Recipe

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

def add_recipe(request):

    if request.method == 'POST':
        title = request.POST['title']
        ingredients = request.POST['ingredients']
        instructions = request.POST['instructions']

        print("Title:", title)
        print("Ingredients:", ingredients)
        print("Instructions:", instructions)

        Recipe.objects.create(
            title=title,
            ingredients=ingredients,
            instructions=instructions
)
        return redirect('recipe_list')

    return render(request, 'addrecipe.html')

def edit_recipe(request, recipe_id):

    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == 'POST':
        title = request.POST['title']
        ingredients = request.POST['ingredients']
        instructions = request.POST['instructions']

        recipe.title = title
        recipe.ingredients = ingredients
        recipe.instructions = instructions

        recipe.save()
        return redirect('recipe_list')

    return render(request, 'editrecipe.html', {
        'recipe': recipe
    })

def delete_recipe(request, recipe_id):

    recipe = Recipe.objects.get(id=recipe_id)

    recipe.delete()

    return redirect('recipe_list')