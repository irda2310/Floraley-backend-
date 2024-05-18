# Generated by Django 4.2.1 on 2023-05-22 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplikacioni', '0006_fullblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_emri', models.CharField(blank=True, max_length=60, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_comment', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]