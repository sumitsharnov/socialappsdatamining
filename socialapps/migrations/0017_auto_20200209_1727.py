# Generated by Django 3.0 on 2020-02-09 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapps', '0016_myinformation_number_of_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='myinformation',
            name='like_link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='myinformation',
            name='like_subject',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
