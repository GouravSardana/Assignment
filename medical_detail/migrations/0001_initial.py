# Generated by Django 2.0.1 on 2018-10-18 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(max_length=500)),
                ('symptoms', models.TextField(max_length=500)),
                ('causes', models.TextField(max_length=500)),
                ('treatment', models.TextField(max_length=500)),
                ('prevention', models.TextField(max_length=500)),
            ],
        ),
    ]