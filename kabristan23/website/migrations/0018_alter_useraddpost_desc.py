# Generated by Django 4.0.3 on 2022-07-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_kisidetay_images_kisidetay_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddpost',
            name='desc',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]