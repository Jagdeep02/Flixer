# Generated by Django 3.2.6 on 2021-08-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210828_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='Video_image',
            field=models.ImageField(upload_to='course'),
        ),
    ]
