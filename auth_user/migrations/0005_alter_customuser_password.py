# Generated by Django 4.1.5 on 2023-05-23 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0004_remove_customuser_password_hash_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
