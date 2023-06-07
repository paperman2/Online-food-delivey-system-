from django.contrib import admin
from foodtiger.models import Contact
from .models import MenuItem, Category, OrderModel
# Register your models here.
admin.site.site_header = "Food TIGER | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','address','fooditem','added_on']

admin.site.register(Contact,ContactAdmin)

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)
