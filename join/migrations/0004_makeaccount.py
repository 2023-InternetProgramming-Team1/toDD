# Generated by Django 4.2.7 on 2023-11-23 04:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0003_delete_makeaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='makeaccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.ManyToManyField(related_name='makeaccount', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]