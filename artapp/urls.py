from django.urls import path
from artapp.views import GetData,GetQuote,ShowQuote
app_name = 'art/'
urlpatterns = [
    path('saveData/', GetData.as_view(), name="get_the_file"),
    path('quotes/', GetQuote.as_view(), name="get_the_quotes"),
    path('showdata/', ShowQuote.as_view(), name="show_the_data")
]
# allow host