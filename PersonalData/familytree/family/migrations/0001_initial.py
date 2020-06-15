# Generated by Django 3.0.6 on 2020-06-11 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fathername', models.CharField(default='Void', max_length=100)),
                ('mothername', models.CharField(default='Void', max_length=100)),
                ('email_address', models.CharField(max_length=100)),
                ('birthplace', models.CharField(max_length=40)),
                ('residence', models.CharField(max_length=100)),
                ('spousename', models.CharField(max_length=100)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.IntegerField(null=True)),
                ('linkimage', models.ImageField(upload_to='images/')),
                ('globalid', models.CharField(default='1', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familyid', models.CharField(max_length=100, unique=True)),
                ('loginname', models.CharField(default='abc', max_length=100, unique=True)),
                ('password', models.CharField(default='abc', max_length=100)),
                ('familyname', models.CharField(max_length=100)),
                ('linkingimage', models.ImageField(upload_to='images/')),
                ('email_address', models.CharField(default='abc@abc.com', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('globalid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='globalidentification', to='family.Family')),
            ],
        ),
        migrations.AddField(
            model_name='family',
            name='familyid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family.Tree', to_field='familyid'),
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('childid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childid', to='family.Family')),
                ('parentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parentid', to='family.Family')),
            ],
        ),
    ]
