# Generated by Django 4.1.5 on 2023-11-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20231112_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gptentry',
            name='unique_link_url',
            field=models.URLField(blank=True, max_length=1024, unique=True),
        ),
    ]
