# Generated by Django 4.0.8 on 2022-11-18 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_book_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='time',
        ),
    ]