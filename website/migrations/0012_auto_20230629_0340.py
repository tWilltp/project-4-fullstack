# Generated by Django 3.2.19 on 2023-06-29 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20230629_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
