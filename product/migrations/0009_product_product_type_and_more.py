# Generated by Django 4.0.3 on 2022-04-16 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_attr_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='features_price_effective',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_att', to='product.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='product.category'),
        ),
    ]
