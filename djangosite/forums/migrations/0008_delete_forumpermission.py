# Generated by Django 3.1.5 on 2021-02-02 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0007_auto_20210202_1709'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ForumPermission',
        ),
    ]