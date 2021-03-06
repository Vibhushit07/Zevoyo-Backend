# Generated by Django 3.2.2 on 2021-05-26 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='cancelled',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('1', 'Booked'), ('2', 'Cancelled')], default=True, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rooms',
            name='roomType',
            field=models.CharField(choices=[('1', 'Premium'), ('2', 'Deluxe'), ('3', 'Basic')], max_length=50),
        ),
    ]
