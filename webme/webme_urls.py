from django.conf.urls import include, url
from django.conf.urls import url
from . import views

#define the url here

#enroute the url request to corresponding views
#here the mainpage is landing page 

#pattern match when no text in between ^ and $ start and end 
#in url request
urlpatterns =[
url(r'^$',views.main_page ,name = 'main_page'),
url(r'^test.html$',views.test ,name = 'test_page'),

]
