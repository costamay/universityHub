# Generated by Django 2.2 on 2020-07-05 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200705_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(upload_to='mdedia/profile'),
        ),
        migrations.AlterField(
            model_name='projectpost',
            name='project_url',
            field=models.URLField(help_text='enter project live link'),
        ),
    ]
