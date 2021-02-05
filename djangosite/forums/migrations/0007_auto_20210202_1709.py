# Generated by Django 3.1.5 on 2021-02-02 22:09

from django.db import migrations, models
import forums.models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0006_auto_20210202_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='perms',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='perms',
        ),
        migrations.AddField(
            model_name='forumpermission',
            name='cate',
            field=models.ForeignKey(blank=True, null=True, on_delete=forums.models.Category, to='forums.category'),
        ),
        migrations.AddField(
            model_name='forumpermission',
            name='forum',
            field=models.ForeignKey(blank=True, null=True, on_delete=forums.models.Forum, to='forums.forum'),
        ),
    ]