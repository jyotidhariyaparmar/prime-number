# Generated by Django 4.0.6 on 2022-08-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('num', '0002_remove_prime_timestemp_alter_prime_fnum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prime',
            name='fnum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='prime',
            name='lnum',
            field=models.BigIntegerField(),
        ),
    ]
