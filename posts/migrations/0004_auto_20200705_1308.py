# Generated by Django 2.2 on 2020-07-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200705_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='projectpost',
            name='project_image',
            field=models.ImageField(default=False, upload_to='projects'),
        ),
    ]
