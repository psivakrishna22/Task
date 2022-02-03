from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Signup
from django.utils.html import format_html

class SingleView(admin.ModelAdmin):
    
    # def thumbnail(self,object):
    #     return format_html('<img src="{}" width="40" style="border-radius:50px;"/>'.format(object.image.url))
    # thumbnail.short_description='photo'
    list_display=('id','name','dob','email','number','gender','country','image')

admin.site.register(Signup,SingleView)