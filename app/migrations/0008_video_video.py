# Generated by Django 3.2.6 on 2021-09-02 15:11

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
    ]