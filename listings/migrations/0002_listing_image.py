# Generated by Django 4.0 on 2022-04-03 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]