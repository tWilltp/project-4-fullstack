# Generated by Django 3.2.19 on 2023-06-13 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_reviewcomments_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewcomments',
            old_name='comments',
            new_name='reviews',
        ),
    ]
