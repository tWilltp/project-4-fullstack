# Generated by Django 3.2.19 on 2023-06-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20230627_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(default=True, max_length=5, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=True, max_length=3),
        ),
    ]
