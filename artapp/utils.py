
from django.db import connection

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
def read_file_data(file_data):
    #file_data = request.data['file']
    read_file_data = pd.read_csv(file_data)
    logging.info('Read the csv file')
    dict_data = read_file_data.to_dict('dict')
    return dict_data

def clear_table():
    cursor = connection.cursor()
    cursor.execute('TRUNCATE TABLE artapp_information')
    connection.commit()
    # Information.objects.all().delete()


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
        info = Information(date=valid_date, arrival=arrival, departures=departure)
        object_list.append(info)
    Information.objects.bulk_create(object_list)
