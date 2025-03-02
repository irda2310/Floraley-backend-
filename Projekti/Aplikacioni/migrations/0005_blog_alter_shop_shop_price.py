# Generated by Django 4.2.1 on 2023-05-22 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplikacioni', '0004_alter_shop_shop_img_alter_shop_shop_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_title', models.TextField(blank=True, max_length=1000, null=True)),
                ('blog_text', models.TextField(blank=True, max_length=1000, null=True)),
                ('blog_img', models.ImageField(upload_to='blog/')),
                ('blog_date', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True),
        ),
    ]
