# Generated by Django 3.2.20 on 2023-12-21 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
