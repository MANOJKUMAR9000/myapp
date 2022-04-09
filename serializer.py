from rest_framework import serializers
from webapp.models import Books
from rest_framework.serializers import ModelSerializer
class Bookserializers(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields='__all__'


