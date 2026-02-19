import datetime
from http.client import responses

from rest_framework import serializers
from book.models import Book
from rest_framework import serializers
from .models import Book, BookImage
from django.contrib.auth import get_user_model


User = get_user_model()

class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ["id", "image"]

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]



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


class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ["id", "image"]


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

