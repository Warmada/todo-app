# Generated by Django 2.2.7 on 2019-11-06 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='closed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
