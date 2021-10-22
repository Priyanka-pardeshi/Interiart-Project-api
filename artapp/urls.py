from django.urls import path
from artapp.views import GetData
app_name = 'art/'
urlpatterns = [
    path('getfile/', GetData.as_view(), name="get_the_file"),
]