# Generated by Django 2.0.6 on 2018-06-30 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('monthDay', models.IntegerField(default=0)),
                ('month', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Peticion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('nameFigurita', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Posesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('nameFigurita', models.CharField(max_length=10)),
            ],
        ),
    ]
