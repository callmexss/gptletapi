# Generated by Django 4.1.5 on 2023-12-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_gptentry_author_gptentry_welcome_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gptentry',
            name='image_url',
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
    ]