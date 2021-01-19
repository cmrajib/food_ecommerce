# Generated by Django 3.1.4 on 2021-01-15 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('longcontent', models.TextField()),
                ('price', models.FloatField(default=0.0)),
                ('discountprice', models.FloatField(default=0.0)),
                ('stock', models.IntegerField(blank=True, default=0)),
                ('hit', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('shipping', models.CharField(default='1 day shipping. Free pickup', max_length=50)),
                ('Weight', models.CharField(max_length=50)),
                ('DateArrived', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='shop.category')),
            ],
        ),
    ]