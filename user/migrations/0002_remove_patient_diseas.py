# Generated by Django 2.2.5 on 2019-10-02 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='diseas',
        ),
    ]
