from django.shortcuts import render
import csv
from app.settings import *
from pprint import pprint
import copy

with open(FILE_CSV, newline='', encoding='utf_8_sig') as csvfile:
    data_dict = csv.DictReader(csvfile)

with open(FILE_CSV, newline='', encoding='utf_8_sig') as csvfile:
    data_list = csv.reader(csvfile, delimiter=';')
    data_list = list(data_list)

    # for each in data_list:
    #     data = {}
    #     data.update('Год': each[0])
    #
    #
    #     pprint(each)


def inflation_view(request):
    template_name = 'app/inflation.html'
    context = {}
    with open(FILE_CSV, newline='', encoding='utf_8_sig') as csvfile:
        data_dict = csv.DictReader(csvfile, delimiter=';')
        for each in data_dict:
            context.update(each)
        # pprint(context)
        # print(type(context))
        return render(request, template_name, context)