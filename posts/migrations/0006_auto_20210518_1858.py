# Generated by Django 2.2 on 2021-05-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_author_comment_projectpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_image',
            field=models.ImageField(default='user.svg', upload_to='profile'),
        ),
    ]
