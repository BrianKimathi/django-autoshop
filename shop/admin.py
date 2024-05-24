from django.contrib import admin
from .models import Category, Product, Comment, ProductImage, Slide, Vehicle


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Allow adding one extra image by default

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
admin.site.register(Slide)
admin.site.register(Vehicle)
