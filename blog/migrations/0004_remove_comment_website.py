# Generated by Django 3.2.9 on 2021-12-11 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='website',
        ),
    ]
