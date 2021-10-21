# Generated by Django 3.2.6 on 2021-08-28 12:46

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=200)),
                ('video_desc', ckeditor.fields.RichTextField()),
                ('is_Premium', models.BooleanField(default=False)),
                ('Video_image', models.ImageField(upload_to='course.png')),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_module_name', models.CharField(max_length=100)),
                ('video_desc', ckeditor.fields.RichTextField(max_length=300)),
                ('can_view', models.BooleanField(default=False)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.video')),
            ],
        ),
        migrations.DeleteModel(
            name='Videos',
        ),
    ]