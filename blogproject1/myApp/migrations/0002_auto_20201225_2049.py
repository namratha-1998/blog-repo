# Generated by Django 2.2 on 2020-12-25 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=264, unique_for_date='publish'),
        ),
    ]
