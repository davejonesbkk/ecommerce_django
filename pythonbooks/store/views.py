from django.shortcuts import render
from django.conf import settings

import bottlenose

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Category
from django.views import generic

import requests
import xml.etree.ElementTree as ET 

from .forms import SubmitBook
from .serializer import BookSerializer

from rest_framework import routers, serializers, viewsets
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

AWS_ACCESS_KEY = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_ASSOCIATE_TAG = ''

amazon = bottlenose.Amazon(AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG)


#class BookViewSet(viewsets.ModelViewSet):

def save_book(request):

	

	if request.method == "POST":
		form = 	SubmitBook(request.POST)
		if form.is_valid():

			item_id = form.cleaned_data['item_id']
			response = amazon.ItemLookup(ItemId=item_id, ResponseGroup='ItemAttributes,Images')
			serializer = BookSerializer(data=response)

			print(serializer)

			if serializer.is_valid():
				embed = serializer.save()
				return render(request, 'embeds.html', {'embed': embed})
	else:
		form = SubmitBook()

	return render(request, 'index.html', {'form': form})




