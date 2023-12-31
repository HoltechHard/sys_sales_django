# Generated by Django 4.2.2 on 2023-07-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appSales", "0004_banner_remove_product_price_productattribute"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="image",
            field=models.ImageField(upload_to="media/images/brand/"),
        ),
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(upload_to="media/images/category/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="media/images/product/"),
        ),
    ]
