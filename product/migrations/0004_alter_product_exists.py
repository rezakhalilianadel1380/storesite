# Generated by Django 4.0.3 on 2022-04-10 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_prict_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='exists',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
