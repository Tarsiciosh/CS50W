# Generated by Django 3.0.6 on 2020-05-12 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200512_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='isModel',
            field=models.BooleanField(default=False),
        ),
    ]
