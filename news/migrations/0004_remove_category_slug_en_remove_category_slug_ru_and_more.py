# Generated by Django 5.2.3 on 2025-06-28 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_name_en_category_name_ru_category_name_uz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug_uz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='slug_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='slug_uz',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='slug_ru',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='slug_uz',
        ),
    ]
