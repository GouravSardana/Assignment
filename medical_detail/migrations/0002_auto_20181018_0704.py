# Generated by Django 2.0.1 on 2018-10-18 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical_detail', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='kDisease',
            new_name='Disease',
        ),
    ]