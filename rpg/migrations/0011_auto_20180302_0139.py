# Generated by Django 2.0.2 on 2018-03-02 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0010_auto_20180228_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='class_name',
            new_name='character_class',
        ),
    ]
