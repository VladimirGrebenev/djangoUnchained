# Generated by Django 3.1.7 on 2021-03-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210307_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=250),
        ),
    ]
