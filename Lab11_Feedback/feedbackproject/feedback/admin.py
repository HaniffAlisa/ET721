from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Item, Feedback

admin.site.register(Item)
admin.site.register(Feedback)