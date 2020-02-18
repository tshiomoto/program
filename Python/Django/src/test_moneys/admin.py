from django.contrib import admin
from .models import Item, Buying, Person

# Register your models here.
admin.site.register(Item)
admin.site.register(Buying)
admin.site.register(Person)