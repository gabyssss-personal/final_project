from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required# Create your views here.

# restrict access through deco. for auth users
from django.contrib.auth.decorators import login_required
from final_project.models import Recipe

from .models import Recipe
from .forms import RecipeForm


@login_required
def home_view(request):
    return render(request, 'home.html')



#custom login page + custom registration page

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
            form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render (request, "register.html", {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'home.html')


# create + edit + edit + delete recipes
# restrict access to auth. user using @login_required deco. (imported above)


# review
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {'recipes': recipes})


# review
@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=True)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})


@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
# prevent the other to edit the recipe NOT owned by them
    if recipe.author != request.user:
        return redirect('recipe_list')
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('recipe_list')
    return render(request, 'recipe_form.html', {'form': form})



@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.author == request.user:
        recipe.delete()
    return redirect('recipe_list')



