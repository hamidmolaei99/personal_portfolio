# Generated by Django 4.1.6 on 2023-03-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('date', models.DateField()),
            ],
        ),
    ]
