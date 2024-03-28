from .models import Transaction
from rest_framework import serializers

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Transaction
        fields='__all__'