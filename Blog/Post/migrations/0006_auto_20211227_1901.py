# Generated by Django 3.2.9 on 2021-12-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0005_blogpost_img1'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='img1',
            field=models.ImageField(upload_to='images'),
        ),
    ]
