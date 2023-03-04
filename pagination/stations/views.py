from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    data_list = []

    with open('data-398-2018-08-30.csv', newline='', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            info_dict = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            data_list.append(info_dict)

    paginator = Paginator(data_list, 10)
    page = paginator.get_page(page_number)

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
