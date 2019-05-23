# Generated by Django 2.2.1 on 2019-05-21 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toolname', models.CharField(max_length=250)),
                ('type_of_tool', models.CharField(max_length=250)),
                ('owner', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('model_pic', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
            ],
        ),
    ]
