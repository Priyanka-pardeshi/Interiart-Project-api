import json
import pandas as pd
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from artapp.utils import date_validation


# import pandas and read csv file
# Create your views here.

class GetData(APIView):
    def get(self, request):
        # read file from json and save it to database
        file_data = request.data['file']
        read_file_data = pd.read_csv(file_data)
        print(read_file_data)
        # reading first column which is date
        fst_col = read_file_data[read_file_data.columns[0]].to_numpy()
        # converting into to list
        list_date = fst_col.tolist()

        # print(list_date)
        list_validates_dates = date_validation(list_date)
        print("Validated dates::",list_validates_dates)
        return Response({'file information': read_file_data})
