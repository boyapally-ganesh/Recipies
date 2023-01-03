# Generated by Django 4.0.1 on 2023-01-01 06:52

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=product.models.get_file_path)),
                ('description', models.TextField(max_length=300)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('mate_description', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(default='Chiken', max_length=150)),
                ('recipe_image', models.ImageField(blank=True, null=True, upload_to=product.models.get_file_path)),
                ('small_description', models.TextField(max_length=250)),
                ('description', models.TextField(default='These crispy Cheddar waffles combine with chicken tenders and a spicy blackberry-muddled maple syrup for a sophisticated version of a classic Southern dish thats also gluten free!', max_length=300)),
                ('prep_time', models.TimeField(default='15:20')),
                ('Total_Time', models.TextField(default='30:30')),
                ('Servings', models.IntegerField(default='8')),
                ('Published_at', models.DateTimeField(auto_now_add=True)),
                ('Ingredients', ckeditor.fields.RichTextField(default='some chicken')),
                ('Main_ingredient', models.CharField(default='chiken', max_length=100)),
                ('Directions', ckeditor.fields.RichTextField(default='thsi is directions')),
                ('Cook_note', models.CharField(max_length=400)),
                ('category', models.ForeignKey(default='Non-veg', on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]