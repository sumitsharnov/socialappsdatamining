# Generated by Django 3.0 on 2020-02-11 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialapps', '0020_item_image_file_load'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image_file_load',
            new_name='image_file_upload',
        ),
    ]
