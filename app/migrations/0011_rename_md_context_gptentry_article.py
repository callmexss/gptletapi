# Generated by Django 4.1.5 on 2023-11-10 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_gptentry_md_context_alter_gptentry_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gptentry',
            old_name='md_context',
            new_name='article',
        ),
    ]
