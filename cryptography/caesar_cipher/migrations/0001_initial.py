# Generated by Django 3.2.7 on 2021-12-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ccDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cipher', models.CharField(max_length=550)),
                ('key', models.IntegerField()),
            ],
        ),
    ]
