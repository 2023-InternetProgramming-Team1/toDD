# Generated by Django 4.2.7 on 2023-11-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_post_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='d_day',
            field=models.IntegerField(default=0),
        ),
    ]
