# Generated by Django 4.1.5 on 2023-05-23 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0003_customuser_password_hash_alter_customuser_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='password_hash',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
