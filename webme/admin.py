from django.contrib import admin

# Register your models here.
#import class webme  from file models in the sourcefolder ie why .import
from .models import webme

admin.site.register(webme)