# Generated by Django 4.0.1 on 2022-01-24 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('birth_date', models.DateField()),
                ('phone', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='customer',
        ),
        migrations.AddField(
            model_name='users',
            name='first_name',
            field=models.TextField(default=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trainer',
            name='first_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='last_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.TextField(),
        ),
    ]