# Generated by Django 4.2.7 on 2023-11-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_category_post_author_alter_post_deadline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]