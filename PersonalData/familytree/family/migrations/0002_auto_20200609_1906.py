# Generated by Django 3.0.6 on 2020-06-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='globalid',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='tree',
            name='loginname',
            field=models.CharField(default='abc', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='tree',
            name='password',
            field=models.CharField(default='abc', max_length=100),
        ),
    ]