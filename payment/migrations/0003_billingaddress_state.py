# Generated by Django 3.1.4 on 2021-01-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20210115_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='state',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]