# Generated by Django 4.0.6 on 2022-08-26 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foradmin', '0004_alter_admin_date_block_date_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_date_block',
            name='date_block',
            field=models.CharField(max_length=100),
        ),
    ]
