# Generated by Django 2.2.6 on 2019-11-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
