# Generated by Django 2.2.7 on 2019-11-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
