# Generated by Django 3.2.9 on 2021-12-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='description',
            field=models.TextField(max_length=10000),
        ),
    ]