# Generated by Django 4.0.8 on 2022-12-06 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0033_alter_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-date_time'], 'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
