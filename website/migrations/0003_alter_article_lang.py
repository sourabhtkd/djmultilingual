# Generated by Django 4.1.5 on 2023-01-29 16:32

import core.constants
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_article_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='lang',
            field=models.CharField(choices=[('en', 'en'), ('hi', 'hi')], default=core.constants.LanguageChoice.get_default, max_length=2),
        ),
    ]