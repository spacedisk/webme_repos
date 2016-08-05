from django.shortcuts import render
import serial

# Create your views here.
def main_page(request):
	return render(request,'webme/main_page.html',{})

def test_page(request):
	return render(request,'webme/test_page.html',{})

