# Generated by Django 3.1 on 2020-08-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_job', '0002_auto_20200821_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]