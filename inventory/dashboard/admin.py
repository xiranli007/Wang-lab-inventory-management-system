from django.contrib import admin
from .models import Inventory, Order, Request, Culture

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'orderedDate']
class RequestAdmin(admin.ModelAdmin):
    list_display= ['name', 'quantity', 'catelogNumber']
class CultureAdmin(admin.ModelAdmin):
    list_display= ['organism', 'idNumber', 'description', 'isolationSource']

admin.site.register(Inventory, ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Request,RequestAdmin)
admin.site.register(Culture,CultureAdmin)

# Register your models here.
