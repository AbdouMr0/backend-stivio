from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'available_sizes', 'image_url')  # Customize as needed

admin.site.register(Product, ProductAdmin)