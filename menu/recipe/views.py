from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Recipe


# Home Page
def home(request):
    return render(request, 'home.html', {
        'name': 'Pranav'
    })


# Recipe List
def recipe_list(request):

    search = request.GET.get('search')

    if search:
        recipes = Recipe.objects.filter(title__icontains=search)
    else:
        recipes = Recipe.objects.all()

    return render(request, 'recipes.html', {
        'recipes': recipes
    })


# Recipe Detail
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    return render(request, 'recipe_detail.html', {
        'recipe': recipe
    })


# Add Recipe
def add_recipe(request):

    if request.method == 'POST':
        title = request.POST['title']
        ingredients = request.POST['ingredients']
        instructions = request.POST['instructions']
        image = request.FILES.get('image')

        # Debug prints
        print("FILES:", request.FILES)
        print("Image:", image)
        print("Title:", title)
        print("Ingredients:", ingredients)
        print("Instructions:", instructions)

        Recipe.objects.create(
            title=title,
            ingredients=ingredients,
            instructions=instructions,
            image=image
        )
        messages.success(request, "Recipe added successfully!")
        return redirect('recipe_list')

    return render(request, 'addrecipe.html')


# Edit Recipe
def edit_recipe(request, recipe_id):

    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == 'POST':

        recipe.title = request.POST['title']
        recipe.ingredients = request.POST['ingredients']
        recipe.instructions = request.POST['instructions']

        # If a new image is uploaded, replace the old one
        if request.FILES.get('image'):
            recipe.image = request.FILES['image']

        recipe.save()
        messages.success(request, "Recipe updated successfully!")

        return redirect('recipe_list')

    return render(request, 'editrecipe.html', {
        'recipe': recipe
    })


# Delete Recipe
def delete_recipe(request, recipe_id):

    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == 'POST':
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect('recipe_list')

    return render(request, 'deleterecipe.html', {
        'recipe': recipe
    })