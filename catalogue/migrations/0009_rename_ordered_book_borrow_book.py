# Generated by Django 4.0.8 on 2022-12-10 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_rename_author_borrow_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrow',
            old_name='ordered_book',
            new_name='book',
        ),
    ]
