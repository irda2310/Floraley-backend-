# Generated by Django 4.2.1 on 2023-05-24 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplikacioni', '0009_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_cel',
        ),
    ]
