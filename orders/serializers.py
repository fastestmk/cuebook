from .models import OrderDetail
from rest_framework.serializers import ModelSerializer

class OrderSerializer(ModelSerializer):

    class Meta:
        model = OrderDetail
        exclude = ('active', 'created', 'modified',)