# Generated by Django 3.0 on 2020-02-09 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapps', '0015_auto_20200209_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='myinformation',
            name='number_of_friends',
            field=models.IntegerField(null=True),
        ),
    ]