from django.contrib import admin
from stock.models import *

# Register your models here.

admin.site.register([Category, Product])

""" @admin.register(Category, Product)
class GenericAdmin(admin.ModelAdmin):
    pass
 """