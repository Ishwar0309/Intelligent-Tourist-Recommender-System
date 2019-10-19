from django.contrib import admin
from tourism.models import fileData, Hotel , Restaurant,Cart
# Register your models here.
admin.site.register(fileData)
admin.site.register(Hotel)
admin.site.register(Restaurant)
admin.site.register(Cart)