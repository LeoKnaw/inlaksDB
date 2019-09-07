# Generated by Django 2.2.4 on 2019-08-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inlaks_app', '0005_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='atm',
            name='atm_or_pos',
            field=models.BooleanField(choices=[(True, 'ATM'), (False, 'POS')], default=True),
            preserve_default=False,
        ),
    ]
