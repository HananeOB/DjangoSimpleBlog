# Generated by Django 3.0.2 on 2020-02-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200204_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='model_pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]