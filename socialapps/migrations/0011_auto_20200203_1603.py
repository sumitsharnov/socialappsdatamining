# Generated by Django 3.0 on 2020-02-03 21:03

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapps', '0010_auto_20200203_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_file',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
        ),
    ]
