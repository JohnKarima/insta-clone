# Generated by Django 3.1.2 on 2020-10-17 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0005_auto_20201017_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
