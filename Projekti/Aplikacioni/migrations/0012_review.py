# Generated by Django 4.2 on 2023-06-11 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplikacioni', '0011_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_name', models.CharField(blank=True, max_length=50, null=True)),
                ('review_job', models.TextField(blank=True, max_length=500, null=True)),
                ('review_message', models.TextField(blank=True, max_length=500, null=True)),
                ('review_img', models.ImageField(upload_to='blog/')),
                ('review_stars', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
