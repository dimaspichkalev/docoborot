# Generated by Django 2.2.6 on 2019-10-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_stockitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]