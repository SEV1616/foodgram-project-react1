import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Команда загружает ингредиенты в базу данных из csv-файла'

    def handle(self, *args, **options):
        data_path = settings.BASE_DIR
        with open(
            f'{data_path}/data/ingredients.csv',
            'r',
            encoding='utf-8'
        ) as file:
            reader = csv.reader(file)
            try:
                Ingredient.objects.bulk_create(
                    Ingredient(
                        name=item[0],
                        measurement_unit=item[1]) for item in reader
                )
            except Exception as e:
                return f'Возникла ошибка при импорте из csv-файла: {e}'

        return (
            f'Загрузка прошла успешно,'
            f'всего загружено ингредиентов - {Ingredient.objects.count()}'
        )
