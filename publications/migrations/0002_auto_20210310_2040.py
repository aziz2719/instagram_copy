# Generated by Django 3.1.7 on 2021-03-10 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publications',
            options={'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
    ]
