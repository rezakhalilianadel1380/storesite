# Generated by Django 4.0.3 on 2022-04-10 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prict',
            new_name='price',
        ),
    ]
