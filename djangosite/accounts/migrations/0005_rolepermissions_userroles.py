# Generated by Django 3.1.5 on 2021-01-26 02:35

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0004_auto_20210121_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='RolePermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perm', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=500)),
                ('perms', models.ManyToManyField(to='accounts.RolePermissions')),
                ('role', models.OneToOneField(on_delete=django.contrib.auth.models.Group, to='auth.group')),
            ],
        ),
    ]