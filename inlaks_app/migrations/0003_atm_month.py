# Generated by Django 2.2.4 on 2019-08-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inlaks_app', '0002_auto_20190827_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='atm',
            name='month',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
