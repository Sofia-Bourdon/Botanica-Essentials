# Generated by Django 3.2.20 on 2023-10-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                (
                    'timestamp',
                    models.DateTimeField(auto_now_add=True)
                ),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('OPEN', 'Open'),
                            ('IN_PROGRESS', 'In Progress'),
                            ('CLOSED', 'Closed')
                        ],
                        max_length=20
                    )
                ),
            ],
        ),
    ]
