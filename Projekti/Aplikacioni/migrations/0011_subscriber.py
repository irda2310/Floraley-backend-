# Generated by Django 4.2.1 on 2023-05-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplikacioni', '0010_remove_contact_contact_cel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
