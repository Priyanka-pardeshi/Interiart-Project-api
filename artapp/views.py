from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# import pandas and read csv file
# Create your views here.

class GetData(APIView):
    def get(self, request):
        # read file from json and save it to database
        file_data = request.data
        print(file_data)
        file = file_data.get('file')
        print(file)

        return Response({'file information': file_data})
