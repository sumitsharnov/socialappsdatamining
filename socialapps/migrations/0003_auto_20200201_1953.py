# Generated by Django 3.0 on 2020-02-02 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapps', '0002_auto_20200201_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
