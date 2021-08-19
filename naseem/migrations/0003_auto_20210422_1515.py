# Generated by Django 3.1.7 on 2021-04-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naseem', '0002_auto_20210422_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='desc',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
