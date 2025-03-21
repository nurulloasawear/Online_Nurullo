# Generated by Django 5.1.6 on 2025-03-08 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorys', '0005_rename_is_optional_categorys_is_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('sorting', models.SmallIntegerField(unique=True)),
            ],
        ),
    ]
