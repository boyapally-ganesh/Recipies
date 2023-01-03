from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import recipe
class customuserform(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'con_password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
class add_recipe(forms.ModelForm):
    class Meta:
        model = recipe
        fields = '__all__'
# class editrecipe_recipe(forms.ModelForm):
#     class Meta:
#         model = recipe
#         fields = '__all__'
class editrecipe(forms.ModelForm):
    class Meta:
        model = recipe
        fields = ['recipe_name','recipe_image','small_description','description','category','prep_time','Total_Time', 'Servings','Ingredients','Main_ingredient','Directions','Cook_note','user']
        small_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'class':'form-control'}))
        description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'class':'form-control'}))
        Directions = forms.CharField(widget=forms.Textarea())
        Ingredients = forms.CharField(widget=forms.Textarea())
        Cook_note = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'class':'form-control'}))
        recipe_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        prep_time = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
        Total_Time = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
        Servings = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
        # widgets = {
        #     'recipe_name':forms.TextInput(attrs={'class':'form-control'}),
        #     'small_description':forms.Textarea(attrs={'class':'form-control',"rows":"3"}), 
        #     # 'recipe_image':forms.ImageField(attrs={'class':'form-control'}),
            
        #     # 'body':forms.Textarea(attrs={'class':'form-control'}),
        #     'user':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder',"type":'hidden'}),
        #    # 'authour':forms.Select(attrs={'class':'form-control'}),
        #     'category':forms.Select(attrs={'class':'form-control'}),
        #     'description':forms.Textarea(attrs={'class':'form-control',"rows":"3"}),
        #     'prep_time':forms.IntegerField(attrs={'class':'form-control'}),
        #     'Total_Time':forms.IntegerField(attrs={'class':'form-control'}),
        #     'Servings':forms.IntegerField(attrs={'class':'form-control'}),
        #     'Main_ingredient':forms.IntegerField(attrs={'class':'form-control'}),
        #     'Directions':forms.Textarea(attrs={'class':'form-control'}),
        #     'Ingredients':forms.Textarea(attrs={'class':'form-control'}),
        #    " Cook_note":forms.Textarea(attrs={'class':'form-control'}),
           
        # }
