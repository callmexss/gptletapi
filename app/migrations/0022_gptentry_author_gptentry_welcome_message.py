# Generated by Django 4.1.5 on 2023-11-25 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_gptentry_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='gptentry',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='gptentry',
            name='welcome_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
