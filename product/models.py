from django.db import models
from django.contrib.auth.models import User
import datetime
import os
from ckeditor.fields import RichTextField

# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    nowtime = datetime.datetime.now().strftime('%Y%m%d%h,:%M:%S')
    filename = '%s%s' % (nowtime, original_filename)
    return os.path.join('uploads/', filename)


# class Category(models.Model):
#     slug = models.CharField(max_length=150, null=False, blank=False)
#     name = models.CharField(max_length=150, null=False, blank=False)
#     image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
#     description = models.TextField(max_length=300, null=False, blank=False)
#     #this is for degital marketing purpose
#     meta_title = models.CharField(max_length=150, null=False, blank=False)
#     meta_keywords = models.CharField(max_length=150, null=False, blank=False)
#     mate_description = models.TextField(max_length=300, null=False, blank=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
class recipe(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     MY_CHOICES = (
        ('veg', 'veg'),
        ('Non_veg', 'Non_veg'),
        
    )
     category = models.CharField(choices=MY_CHOICES, max_length=10, default="Non_veg")
     recipe_name = models.CharField(max_length=150, null=False, blank=False, default='Chiken')
     recipe_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
     small_description = models.TextField(max_length=250, null=False, blank=False)
     description = models.TextField(max_length=300, null=False, blank=False, default='These crispy Cheddar waffles combine with chicken tenders and a spicy blackberry-muddled maple syrup for a sophisticated version of a classic Southern dish thats also gluten free!')
     prep_time = models.IntegerField(default='15')
     Total_Time = models.IntegerField(default='30')
     Servings = models.IntegerField(default='8', null=False,blank=False)
     Published_at =  models.DateTimeField(auto_now_add=True, blank=False)
     Ingredients = RichTextField(default="some chicken",blank=False, null=False)
     Main_ingredient = models.CharField(max_length=100,default="chiken", null=False, blank=False)
     Directions = RichTextField(blank=False, null=False, default="thsi is directions")
     Cook_note = models.CharField(max_length=400,blank=False, null=False)
     def __str__(self):
            return self.recipe_name
     def get_absolute_url(self):
        return reverse('home')