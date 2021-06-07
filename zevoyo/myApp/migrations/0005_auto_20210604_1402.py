# Generated by Django 3.2.2 on 2021-06-04 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_auto_20210527_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Booked', 'Booked'), ('Cancelled', 'Cancelled')], max_length=15),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='roomType',
            field=models.CharField(choices=[('Premium', 'Premium'), ('Deluxe', 'Deluxe'), ('Basic', 'Basic')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], max_length=15),
        ),
    ]
