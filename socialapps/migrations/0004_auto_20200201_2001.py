# Generated by Django 3.0 on 2020-02-02 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapps', '0003_auto_20200201_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(upload_to='images'),
        ),
    ]
