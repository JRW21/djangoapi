#This is the serializer page
from rest_framework import serializers
from .models import Book
#class BookSerializer(serializers.ModelSerializer):#adding in Hyperlinked part in order to access url in serializer
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields =('id','url','title','pub_date')
        