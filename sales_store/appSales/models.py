from django.db import models
from distutils.command.upload import upload

# Create your models here.
from django.utils.html import mark_safe

class Banner(models.Model):
    img = models.ImageField(upload_to = 'appSales/static/images/banner/')
    alt_text = models.CharField(max_length = 300)

    def image_tag_path(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.alt_text

class Category(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'appSales/static/images/category/')

    def image_tag_path(self):
        return mark_safe('<img src="%s" width="80" height="80" />' % (self.image.url))

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'appSales/static/images/brand/')

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length = 40)
    code = models.CharField(max_length = 40)

    def color_tag_path(self):
        return mark_safe('<div style="width:50px; height:50px; background:%s"></div>' % (self.code))

    def __str__(self):
        return self.title
    
class Size(models.Model):
    title = models.CharField(max_length = 40)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'appSales/static/images/product/')
    slug = models.CharField(max_length = 400)
    detail = models.TextField()
    specs = models.TextField()

    # foreign keys     
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    color = models.ForeignKey(Color, on_delete = models.CASCADE)
    size = models.ForeignKey(Size, on_delete = models.CASCADE)

    # flag
    status = models.BooleanField(default = True)
    is_featured = models.BooleanField(default = False)

    def __str__(self):
        return self.title
    
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    color = models.ForeignKey(Color, on_delete = models.CASCADE)
    size = models.ForeignKey(Size, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits = 8, decimal_places = 2, default = 0.0)

    def __str__(self):
        return self.product.title
