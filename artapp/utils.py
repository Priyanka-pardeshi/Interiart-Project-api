

import datetime

from artapp.models import Information

'''
This function takes date field and validate and return validated Date
'''


def date_validation(date):
    string = date.replace('M', '')
    year = string[0:4]
    month = string[4:]
    x = datetime.datetime(int(year), int(month), 13)
    valid_date = x.strftime('%Y-%m-%d %H:%M:%S')
    return valid_date


'''
'''


def clear_table():
    Information.objects.all().delete()


'''
This function save bulk of data to database.
'''


def save_data(dict_data):
    date_list = dict_data['Date'].values()
    arrival_list = dict_data['ArrivalsActualCounts'].values()
    departure_list = dict_data['ArrivalsActualCounts'].values()
    object_list = []
    # iterate through 3 list, create object
    for (dates, arrival, departure) in zip(date_list, arrival_list, departure_list):
        print(dates, arrival, departure)
        valid_date = date_validation(dates)
        info = Information(date=valid_date, Arrival=arrival, Departures=departure)
        object_list.append(info)
    Information.objects.bulk_create(object_list)
