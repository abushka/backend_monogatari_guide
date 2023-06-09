# Generated by Django 4.1.5 on 2023-06-01 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_alter_chapter_name_en_alter_chapter_name_jp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='volume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='worker.volume'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='worker.season'),
        ),
    ]
