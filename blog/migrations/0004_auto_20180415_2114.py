# Generated by Django 2.0.4 on 2018-04-15 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_file_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='file',
            name='post',
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
