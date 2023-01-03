from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import customuserform, add_recipe, editrecipe
from .models import recipe
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import json

def register(request):
    form = customuserform()
    if request.method == 'POST':
        form = customuserform(request.POST)
        if form.is_valid():
            form.save()
            message = 'registered successfully ! login to continue'
            return redirect('/login/')
            messages.success(request, message)
    context = {'form':form}
    return render(request, "product/register.html", context)

def login_view(request):
    if not request.user.is_authenticated:
      if request.method == 'POST':
         lg = AuthenticationForm(request=request, data=request.POST)
         if lg.is_valid():
            uname=lg.cleaned_data['username']
            upass=lg.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
               login(request, user)
               messages.success(request, 'logged in successfully')
              
               return HttpResponseRedirect('/')
      else:
        messages.error(request, 'invalid username or password')
        lg = AuthenticationForm()
      return render(request, 'product\login.html',{'form':lg})
    else:
        messages.warning(request, "you are already logged in")
        return HttpResponseRedirect('/')

#logout
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'logged out successfully')
    return HttpResponseRedirect('/')
def main(request):
    recipes = recipe.objects.all()
    context = {'recipe':recipes}
    return render(request, 'product/main.html',context)
def account(request):
  
    myrecipe = recipe.objects.filter(user=request.user)
    context = {'myrecipes':myrecipe}
    return render(request, 'product/account.html', context)
login_required('login/')
def addyourrecipe(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = add_recipe(request.POST)
            if form.is_valid():
                form.save()
                return redirect('account/')
        else:
            form = add_recipe()
        context = {'form':form}
        return render(request, 'product/addrecipe.html',context)
    else:
        return HttpResponseRedirect('/login/')
# def edit_post_view(request, pk, slug):
#     Recipe = get_object_or_404(recipe, recipe_name=slug, pk=pk)
#     if request.method == 'POST':
#         form = editrecipe_recipe(request.POST, instance=Recipe)
#         if form.is_valid():
#             form.save()
#             return redirect('acount/', recipe_name=recipe.recipe_name,  id=recipe.pk, )
#     else:
#         form = editrecipe_recipe(instance=pk)
#     return render(request, 'product\editrecipe.html', {'form': form})
# def editrecipe(request, pk):
#     Recipe = recipe.objects.get(id=pk)

#     if request.method == "POST":
#         if len(request.FILES) != 0:
#             if len(Recipe.recipe_image) > 0:
#                 os.remove(Recipe.recipe_name.path)
#             Recipe.recipe_image = request.FILES['recipe_image']

#         Recipe.category = request.POST.get['category']
#         Recipe.recipe_name = request.POST.get['recipe_name']
#         Recipe.small_description = request.POST.get['small_description']
#         Recipe.description = request.POST.get['description']
#         Recipe.prep_time = request.POST.get['prep_time']
#         Recipe.Total_Time = request.POST.get['Total_Time']
#         Recipe.Servings = request.POST.get['Servings']
#         Recipe.Ingredients = request.POST.get['Ingredients']
#         Recipe.Main_ingredient = request.POST.get['Main_ingredient']
#         Recipe.Directions = request.POST.get['Directions']
#         Recipe.Cook_note = request.POST.get['Cook_note']
#         Recipe.save()
#         messages.success(request, 'recipe updated successfully!')
#         redirect('account/')
#     context = {'prod':Recipe}
#     return render(request, 'product\editrecipe.html', context)
# def editrecipe(request, pk):
#     Recipe = get_object_or_404(recipe, pk=pk)
#     if request.method == 'POST':
#         if len(request.FILES) != 0:
#                 if len(Recipe.recipe_image) > 0:
#                     os.remove(Recipe.recipe_name.path)
#                 Recipe.recipe_image = request.FILES['recipe_image']
#         Recipe.category = request.POST.get['category']
#         Recipe.recipe_name = request.POST.get['recipe_name']
#         Recipe.small_description = request.POST.get['small_description']
#         Recipe.description = request.POST.get['description']
#         Recipe.prep_time = request.POST.get['prep_time']
#         Recipe.Total_Time = request.POST.get['Total_Time']
#         Recipe.Servings = request.POST.get['Servings']
#         Recipe.Ingredients = request.POST.get['Ingredients']
#         Recipe.Main_ingredient = request.POST.get['Main_ingredient']
#         Recipe.Directions = request.POST.get['Directions']
#         Recipe.Cook_note = request.POST.get['Cook_note']
       
#         Recipe.save()
#         return redirect('account/')
#     return render(request, 'product/editrecipe.html', {'prod': Recipe})
# def editrecipe(request, pk, instance=None):
#     recipe_id = recipe.objects.get(id=pk)
#     form = editrecipe(instance=recipe_id)
#     context ={'prod':form}
#     return render(request, 'product/editrecipe.html', context)
def editrecipe(request, pk):
    recipes = get_object_or_404(recipe, id=pk)
    if request.method == 'POST':
        # Create a form instance with the POST data and the instance as the initial data
        form = editrecipe(request.POST, instance=recipes)
        # Validate the form
        if form.is_valid():
            # Save the form and redirect to a success page
            form.save()
            return redirect('/')
    else:
        # Create a form instance with the instance as the initial data
        form = editrecipe(instance=recipes)
    # Render the form template with the form instance as context
    return render(request, 'product/editrecipe.html', {'prod': form})
def detail_view(request, pk):
    if(recipe.objects.filter(id=pk)):
          detail_item = recipe.objects.filter(id=pk).first()
          context = {'detail':detail_item}
    else:
        messages.error(request, 'no such category found')
        
        return redirect("/")
    return render(request, 'product/detailview.html', context)
def search_items(request):
    if request.method == "POST":
       
        search_str = json.loads(request.body).get("searchText")
        recipe_items = recipe.objects.filter(
            recipe_name__startswith=search_str, user=request.user) | recipe.objects.filter(
                small_description__startswith=search_str, user=request.user) | recipe.objects.filter(
                    Main_ingredient__icontains=search_str, user=request.user) | recipe.objects.filter(
                        category__icontains=search_str, user=request.user
                    )
        data = recipe_items.values()
        return JsonResponse(list(data), safe=False)
       


