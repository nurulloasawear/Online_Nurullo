# Generated by Django 5.1.6 on 2025-04-01 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorys', '0006_brand_region'),
        ('product', '0013_remove_product_brand_remove_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='country_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.country'),
        ),
    ]
