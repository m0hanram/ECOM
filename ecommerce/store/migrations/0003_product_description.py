# Generated by Django 2.2.14 on 2021-02-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='This is a short description about the product'),
            preserve_default=False,
        ),
    ]
