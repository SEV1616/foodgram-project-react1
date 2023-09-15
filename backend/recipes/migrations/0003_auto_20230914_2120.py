# Generated by Django 3.2.6 on 2023-09-14 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='shoppinglist',
            name='unique_recipe_in_user_shopping_list',
        ),
        migrations.RemoveField(
            model_name='shoppinglist',
            name='recipe',
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='recipe',
            field=models.ManyToManyField(related_name='shopping_list', to='recipes.Recipe', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_list', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
