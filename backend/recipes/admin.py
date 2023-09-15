from django.contrib import admin

from .models import (
    Favorite, Ingredient, Recipe, RecipeIngredients, RecipeTags, ShoppingList,
    Tag,
)


EMPTY_MSG = '-пусто-'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'measurement_unit')
    list_filter = ['name']
    search_fields = ('name',)


class RecipeIngredientsInline(admin.TabularInline):
    model = RecipeIngredients
    min_num = 1
    extra = 1


class RecipeTagsInline(admin.TabularInline):
    model = RecipeTags
    min_num = 1
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'author', 'in_favorite')
    list_filter = ['name', 'author', 'tags']
    inlines = (RecipeIngredientsInline, RecipeTagsInline)

    def in_favorite(self, obj):
        return obj.in_favorite.all().count()


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'get_recipe', 'get_count')
    empty_value_display = EMPTY_MSG

    @admin.display(
        description='Рецепты')
    def get_recipe(self, obj):
        return [
            f'{item["name"]} ' for item in obj.recipe.values('name')[:5]]

    @admin.display(
        description='В избранных')
    def get_count(self, obj):
        return obj.recipe.count()


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'get_recipe', 'get_count')
    empty_value_display = EMPTY_MSG

    @admin.display(description='Рецепты')
    def get_recipe(self, obj):
        return [
            f'{item["name"]} ' for item in obj.recipe.values('name')[:5]]

    @admin.display(description='В избранных')
    def get_count(self, obj):
        return obj.recipe.count()
