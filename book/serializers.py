import datetime
from http.client import responses

from rest_framework import serializers
from book.models import Book

class BookSerializer(serializers.ModelSerializer):


    def to_internal_value(self, data):
        data['published_date']=datetime.datetime.strptime(data['published_date'] , '%Y/%m/%d').date()
        data=super().to_internal_value(data=data )
        print(data)
        return data


    def to_representation(self, instance):
        response = super().to_representation(instance=instance)
        print(type(response['published_date']))
        return response


    class Meta:
        model=Book
        fields='__all__'
