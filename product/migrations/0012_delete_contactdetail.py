# Generated by Django 5.1.6 on 2025-04-01 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_country_alter_productimage_product_contactdetail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactDetail',
        ),
    ]
