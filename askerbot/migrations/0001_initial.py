# Generated by Django 4.0.6 on 2022-07-11 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('telegram_id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=16, null=True)),
            ],
        ),
    ]
