# Generated by Django 4.1.7 on 2024-02-29 12:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='timestamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]