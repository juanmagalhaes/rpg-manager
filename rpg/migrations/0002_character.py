# Generated by Django 2.0.1 on 2018-02-21 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('class_name', models.CharField(max_length=100)),
                ('health_points', models.IntegerField()),
                ('level', models.IntegerField()),
                ('magic_points', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('player', models.CharField(max_length=100)),
                ('race', models.CharField(max_length=100)),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rpg.Game')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]