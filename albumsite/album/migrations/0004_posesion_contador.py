# Generated by Django 2.0.6 on 2018-06-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_auto_20180630_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='posesion',
            name='contador',
            field=models.IntegerField(default=1),
        ),
    ]
