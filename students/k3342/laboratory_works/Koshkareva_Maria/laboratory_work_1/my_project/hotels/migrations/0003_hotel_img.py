# Generated by Django 3.0.5 on 2020-04-20 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_auto_20200420_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]