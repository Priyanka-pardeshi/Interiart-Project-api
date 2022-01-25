import pandas as pd
from django.core.exceptions import FieldError
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from artapp.utils import save_data, clear_table
from artapp.serializer import QuoteSerializer
from artapp.models import Information
from django.core.paginator import Paginator
from artapp.models import Information,Quote
import logging

logging.basicConfig(filename='interiArtLogger.log', filemode='w')

# Create your views here.
'''
This class contains POST method which reads  data from csv file and save it into the data base
Returns success message
'''


class GetData(APIView):

    def post(self, request):
        '''
        Following Function performs POST operation.
        Function tread csv file , and Read data from csv File and save that data into database.
        '''
        try:

            file_data = request.data['file']
            read_file_data = pd.read_csv(file_data)
            logging.info('Read the csv file')
            dict_data = read_file_data.to_dict('dict')
            logging.info('Cleared table of database')
            clear_table()
            save_data(dict_data)
            logging.info('after reading file data is saved in database')
            return Response({'message': 'Data is saved.'})
        except PermissionDenied:
            logging.exception('Exception : Authenticated request fails the permission checks')
            return Response({'exception': 'authenticated request fails the permission checks'})
        except NotFound:
            logging.exception('Exception : resource does not exists at the given URL.')
            return Response({'exception': 'resource does not exists at the given URL.'})



'''
    this class save name,phone,email,type_of_property,type_of_services,Message 
'''


class GetQuote(APIView):
    '''
    following function performs POST operation
    It takes Inputs from forms i.e name, phone, email, property, service, message.
    '''
    def post(self, request):
        try:
            serializer = QuoteSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            logging.info('Data is Serialized')
            serializer.save()
            #Quote.objects.raw("Insert into artapp_quote values(%s,%s,%s,%s,%s)",['name','phone','email','property','service'])

            logging.info('Data is saved')
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        except PermissionDenied:
            logging.exception('Exception: authenticated request fails the permission checks')
            return Response({'exception': 'authenticated request fails the permission checks'})
        except NotFound:
            logging.exception('Exception:resource does not exists at the given URL.')
            return Response({'exception': ' resource does not exists at the given URL.'})
        except FieldError:
            logging.exception('Exception: exception is raised due to problem in a model field.')
            return Response({'exception': 'exception is raised due to problem in a model field.'})
        except Exception as exception:
            return Response({'exception': str(exception)})


class ShowQuote(APIView):
    def get(self, request):
        '''
        follwing function perform get operation.
        Function talkes page-number and number of records.
        '''
        try:
            info = Information.objects.all()
            #info=Information.objects.raw("select date,arrival,departures from artapp_information;")
            current_page_number = request.data.get('page') or 1
            number_of_records = request.data.get('number') or 5
            page_number = request.GET.get('page', current_page_number)
            paginator = Paginator(info, number_of_records)
            temp = paginator.page(page_number)
            print(list(temp.object_list.values()))
            # check how many pages
            logging.info('Displaying data using pagination.')
            # {"data":{"travellist":[],"current_page":2}}- response struct
            return Response({'data': list(temp.object_list.values()), 'page':current_page_number})
        except PermissionDenied:
            logging.exception('Exception:authenticated request fails the permission checks')
            return Response({'exception': 'authenticated request fails the permission checks'})
        except NotFound:
            logging.exception('exception: resource does not exists at the given URL.')
            return Response({'exception': ' resource does not exists at the given URL.'})

