# Generated by Django 4.2.1 on 2023-05-24 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplikacioni', '0008_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_message', models.TextField(blank=True, max_length=500, null=True)),
                ('contact_cel', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]