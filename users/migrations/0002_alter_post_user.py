# Generated by Django 3.2.6 on 2021-08-26 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default='Admin', on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
