# Generated by Django 4.1.5 on 2023-11-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_category_tag_gptentry_category_gptentry_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gptentry',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='tag_apps', to='app.tag'),
        ),
    ]
