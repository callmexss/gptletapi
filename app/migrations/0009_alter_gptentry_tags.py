# Generated by Django 4.1.5 on 2023-11-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_gptentry_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gptentry',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tag_apps', to='app.tag'),
        ),
    ]
