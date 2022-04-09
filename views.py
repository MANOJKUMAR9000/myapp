from django.shortcuts import render
from webapp.serializer import Bookserializers
from webapp import models
from rest_framework import request
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView

from webapp.models import Books

# Create your views here.
from rest_framework.generics import ListAPIView

class BookListAPIview(ListAPIView):
    serializer_class = Bookserializers
    def get_queryset(self):
        qs=Books.objects.all()
        manoj=self.request.GET.get(qs)


        return (qs)








class BookCreateView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = Bookserializers

class BookRetriveView(RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = Bookserializers
    lookup_field='id'


class BookUpdateView(UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = Bookserializers
    lookup_field='id'

class BookDestroyView(DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = Bookserializers
    lookup_field='id'


