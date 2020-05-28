# Generated by Django 3.0.6 on 2020-05-22 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='childid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childid', to='family.Family'),
        ),
        migrations.AlterField(
            model_name='child',
            name='parentid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parentid', to='family.Family'),
        ),
    ]