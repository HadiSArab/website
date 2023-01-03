from rest_framework import serializers
from api.models import item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'
