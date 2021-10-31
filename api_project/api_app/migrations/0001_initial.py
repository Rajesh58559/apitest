# Generated by Django 3.2.7 on 2021-10-31 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('main_image', models.ImageField(upload_to='image')),
                ('right_view', models.ImageField(upload_to='image')),
                ('left_view', models.ImageField(upload_to='image')),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField(default=1)),
                ('description', models.TextField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
