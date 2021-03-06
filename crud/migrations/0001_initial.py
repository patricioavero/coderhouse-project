# Generated by Django 4.0.1 on 2022-01-24 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(verbose_name=50)),
                ('last_name', models.TextField(verbose_name=50)),
                ('birth_date', models.DateField()),
                ('phone', models.TextField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(verbose_name=50)),
                ('last_name', models.TextField(verbose_name=50)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.TextField(verbose_name=50)),
            ],
        ),
    ]
