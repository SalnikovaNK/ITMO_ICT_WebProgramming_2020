# Generated by Django 3.0.5 on 2020-06-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0012_auto_20200615_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='teaser',
            field=models.TextField(max_length=400),
        ),
    ]