# Generated by Django 3.0.6 on 2020-05-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=100)),
                ('birthplace', models.CharField(max_length=40)),
                ('residence', models.CharField(max_length=100)),
                ('spousename', models.TextField()),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
    ]
