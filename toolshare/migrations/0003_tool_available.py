# Generated by Django 2.2.1 on 2019-05-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolshare', '0002_auto_20190522_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
