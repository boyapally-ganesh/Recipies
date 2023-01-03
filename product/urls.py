from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('',views.main, name='home'),
    path('register/',views.register, name='register'),
    path('account/',views.account, name = 'account'),
    path('logout/',views.logoutpage, name='logout'),
    path('addrecipe/',views.addyourrecipe, name = 'addrecipe'),
    path('editrecipe/<int:pk>', views.editrecipe, name='editrecipe'),
    path('detail/<int:pk>/',views.detail_view, name ='detail'),
    path('search-recipes',csrf_exempt(views.search_items), name = 'search-recipe'),
]