# Generated by Django 4.1.7 on 2023-04-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('Dept_no', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('Dname', models.CharField(max_length=100)),
                ('loc', models.CharField(max_length=100)),
            ],
        ),
    ]
