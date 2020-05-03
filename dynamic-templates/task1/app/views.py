from django.shortcuts import render
import csv
from app.settings import *

with open(FILE_CSV, newline='', encoding='utf_8_sig') as csvfile:
    data_list = csv.reader(csvfile, delimiter=';')
    data_list = list(data_list)


def inflation_view(request):
    template_name = 'app/inflation.html'
    context = {}
    year_list = list()
    for year in data_list:
        temp_list = []
        for month in year:
            try:
                month = int(month)
                temp_list.append(month)
            except:
                try:
                    month = float(month)
                    temp_list.append(month)
                except:
                    temp_list.append(month)
        year_list.append(temp_list)
    context['rows'] = year_list
    return render(request, template_name, context)