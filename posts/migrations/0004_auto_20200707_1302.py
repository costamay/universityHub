# Generated by Django 2.2 on 2020-07-07 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpost',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='ProjectPost',
        ),
    ]