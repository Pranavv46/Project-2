from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Recipe

#user authentication 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Home Page
def home(request):
    return render(request, 'home.html', {
        'name': 'Pranav'
    })

# User Registration
def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully!")

        return redirect('login')

    return render(request, 'register.html')

def login_user(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(request, "Login successful!")

            return redirect('home')

        else:

            messages.error(request, "Invalid username or password!")

            return redirect('login')

    return render(request, 'login.html')

def logout_user(request):

    logout(request)

    messages.success(request, "Logged out successfully!")

    return redirect('login')


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
@login_required
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
@login_required
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
@login_required
def delete_recipe(request, recipe_id):

    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == 'POST':
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect('recipe_list')

    return render(request, 'deleterecipe.html', {
        'recipe': recipe
    })