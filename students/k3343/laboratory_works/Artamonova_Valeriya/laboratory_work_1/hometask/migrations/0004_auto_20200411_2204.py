# Generated by Django 3.0.5 on 2020-04-11 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hometask', '0003_auto_20200411_2055'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='comment',
            name='post_date',
            field=models.DateField(default='2020-04-09', verbose_name='Дата написания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='hometask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hometask.Hometask', verbose_name='Домашнее задание'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hometask.UserProfile', verbose_name='Автор комментария'),
        ),
    ]
