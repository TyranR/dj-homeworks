import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                mobile = Phone()
                mobile.title = line[1]
                mobile.image = line[2]
                mobile.price = line[3]
                mobile.release_date = line[4]
                mobile.lte_exists = line[5]
                mobile.slug = mobile.sluggg()
                try:
                    mobile.save()
                    print(f'Телефон {mobile} в базу внесён')
                except:
                    print(f'Что-то пошло не так. Телефон {mobile} не был внесён')
