# Generated by Django 3.1.7 on 2021-03-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_hotelroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('available', models.CharField(max_length=1)),
            ],
        ),
    ]