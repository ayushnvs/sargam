# Generated by Django 4.1 on 2022-08-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_alter_singer_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
