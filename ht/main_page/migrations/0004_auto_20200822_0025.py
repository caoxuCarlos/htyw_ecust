# Generated by Django 3.1 on 2020-08-22 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_remove_post_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='introduce',
            field=models.CharField(max_length=200),
        ),
    ]
