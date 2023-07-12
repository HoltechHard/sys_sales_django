from django.contrib import admin

# Register your models here.

from .models import Banner, Category, Brand, Color, Size, Product, ProductAttribute

admin.site.register(Brand)
admin.site.register(Size)

class BannerAdmin(admin.ModelAdmin):
    list_display = ("alt_text", "img")

admin.site.register(Banner, BannerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "image_tag_path")

admin.site.register(Category, CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'color_tag_path')

admin.site.register(Color, ColorAdmin)    

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "brand", "color", "size", "status", "is_featured")
    list_editable = ("status", "is_featured")

admin.site.register(Product, ProductAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "price", "color", "size")

admin.site.register(ProductAttribute, ProductAttributeAdmin)
