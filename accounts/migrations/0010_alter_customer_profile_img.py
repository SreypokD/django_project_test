# Generated by Django 4.2.6 on 2023-10-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_customer_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_img',
            field=models.ImageField(blank=True, default='defual_img.jpg', null=True, upload_to=''),
        ),
    ]