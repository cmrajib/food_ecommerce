# Generated by Django 3.1.4 on 2021-01-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='address',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='address1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='address2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='first_name',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='last_name',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
