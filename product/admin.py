from django.contrib import admin
from .models import Brand, Product, Review

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  
    list_display = ("name", "slug")  

admin.site.register(Brand, BrandAdmin)
admin.site.register(Product)
admin.site.register(Review)


