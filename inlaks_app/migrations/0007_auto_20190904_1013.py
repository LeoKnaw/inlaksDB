# Generated by Django 2.2.4 on 2019-09-04 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inlaks_app', '0006_atm_atm_or_pos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atm',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]