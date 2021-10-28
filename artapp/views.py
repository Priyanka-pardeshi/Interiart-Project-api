import json

import pandas as pd
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from artapp.utils import save_data
from artapp.serializer import QuoteSerializer, InformationSerializer
from artapp.models import Information
from django.core.paginator import Paginator

# Create your views here.
'''
This class contains POST method which reads  data from csv file and save it into the data base
Returns success message
'''


class GetData(APIView):
    def post(self, request):
        try:
            file_data = request.data['file']
            read_file_data = pd.read_csv(file_data)
            dict_data = read_file_data.to_dict('dict')
            print("dict data::", dict_data)
            # clear database table all.delete()
            Information.objects.all().delete()
            saved_message = save_data(dict_data)
            return Response({'message': saved_message})
        except Exception as exception:
            return Response({'message': str(exception)})

    '''
    this class save name,phone,email,type_of_property,type_of_services,Message 
    '''


class GetQuote(APIView):
    def post(self, request):
        try:
            serializer = QuoteSerializer(data=request.data)
            print(serializer)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as exception:
            return {'exception': str(exception)}


class ShowQuote(APIView):
    def get(self, request):
        try:
            info = Information.objects.all()

            # page number and number of records  --- from body
            page_number = request.GET.get('page', 1)
            paginator = Paginator(info, 5)

            temp = paginator.page(page_number)
            print(list(temp.object_list.values()))
            return Response({'message': (list(temp.object_list.values()))})
        except Exception as exception:
            return Response({'exception': str(exception)})


