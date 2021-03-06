# Generated by Django 2.0.1 on 2018-10-20 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medical_detail', '0003_delete_disease'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('symptoms', models.TextField(max_length=500)),
                ('causes', models.TextField(max_length=500)),
                ('diagnosis', models.TextField(max_length=500)),
                ('treatment', models.TextField(max_length=500)),
                ('prevention', models.TextField(max_length=500)),
            ],
        ),
    ]
