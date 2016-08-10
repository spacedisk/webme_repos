from django.shortcuts import render
#from .models import Post #this is to import the  object post of class models 
from django.utils import timezone #so we can query using timezone of published posts
#now we could use quieries to filter order and view instance of this object which are 
#originally posts published in the databse 
""" published posts inherits Post class and Post class inherits from models class
thus posts are objects of Post and Post is an object of models in django DRM"""


# Create your views here.
def main_page(request):
	return render(request,'webme/main_page.html')

def test(request):
	return render(request,'webme/test_page.html')

