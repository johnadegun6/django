from django.contrib import admin
from .models import Products, Store, Category, Rating
from .account.models import Profile

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'total_products')
    list_filter = ('name', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'store', 'Category')
    list_filter = ('Category', 'store' )
    list_per_page = 10


admin.site.register(Products, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Category)
admin.site.register(Rating)