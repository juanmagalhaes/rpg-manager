# Generated by Django 2.0.2 on 2018-02-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0005_auto_20180224_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='avatar',
            field=models.URLField(blank=True, default=''),
        ),
    ]