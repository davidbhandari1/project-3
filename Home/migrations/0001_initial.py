# Generated by Django 4.1.4 on 2022-12-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=300)),
                ('subject', models.TextField(blank=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
