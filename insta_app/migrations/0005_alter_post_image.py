# Generated by Django 4.1.7 on 2023-03-27 23:00

from django.db import migrations, models
import insta_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('insta_app', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/img/grey_background.jpg', upload_to=insta_app.models.upload_to),
        ),
    ]