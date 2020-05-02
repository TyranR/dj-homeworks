from django.shortcuts import render, redirect
from django.urls import reverse
from app.settings import *
from django.conf import settings
from django.core.paginator import Paginator
import csv
import urllib.parse
from pprint import pprint

with open(BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
    all_stations = csv.DictReader(csvfile)
    all_stations = list(all_stations)


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    paginator = Paginator(all_stations, 10)
    current_page = request.GET.get('page', 1)
    print(f'current_page равен {current_page}')
    articles = paginator.get_page(current_page)
    print(f'articles равен {articles}')
    if articles.has_previous():
        prev_page_number = int(current_page)-1
    if articles.has_next():
        next_page_number = int(current_page)+1
    prev_page_url = urllib.parse.urlencode({'page' : prev_page_number})
    next_page_url = urllib.parse.urlencode({'page': next_page_number})
    prev_page_url = 'bus_stations?'+str(prev_page_url)
    next_page_url = 'bus_stations?'+str(next_page_url)
    data = paginator.page(current_page)
    pprint(data.object_list)
    stations = station = {}
    for each in data.object_list:
        station['Name'] = each['Name']
        station['Street'] = each['Street']
        station['District'] = each['District']
        pprint(station)

    return render(None, 'index.html', context={
        'bus_stations': [{'Name': 'Имя', 'Street': 'Улица', 'District': 'Район'}],
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
