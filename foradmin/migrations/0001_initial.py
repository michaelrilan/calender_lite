# Generated by Django 4.0.6 on 2022-08-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_limit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_block', models.DateField()),
                ('entry_limit', models.IntegerField()),
            ],
        ),
    ]
