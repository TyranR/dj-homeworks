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


def inflation_view(request):
    template_name = 'app/inflation.html'
    context = {}
    temp_dict = {}
    # with open(FILE_CSV, newline='', encoding='utf_8_sig') as csvfile:
    #     data_dict = csv.DictReader(csvfile, delimiter=';')
    #     for each in data_dict:
    #         id = each['Год']
    #         temp_dict.update(id: each)
    #         context.update[{each['Год']}: temp_dict]
    #     pprint(context)
    #     print(type(context))
    for year in data_list:
        id = year[0]
        context[id] = year
    pprint(context)
    return render(request, template_name, context)