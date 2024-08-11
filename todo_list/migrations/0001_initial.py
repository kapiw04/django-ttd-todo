# Generated by Django 5.1 on 2024-08-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
