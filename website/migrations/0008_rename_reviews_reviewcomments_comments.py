# Generated by Django 3.2.19 on 2023-06-13 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_rename_comments_reviewcomments_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewcomments',
            old_name='reviews',
            new_name='comments',
        ),
    ]
