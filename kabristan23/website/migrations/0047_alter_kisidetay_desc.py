# Generated by Django 4.0.3 on 2022-07-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0046_kisidetay_adres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kisidetay',
            name='desc',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]