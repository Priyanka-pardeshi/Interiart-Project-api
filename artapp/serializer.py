from rest_framework.serializers import ModelSerializer
from artapp.models import Information, Quote


class InformationSerializer(ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class QuoteSerializer(ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

