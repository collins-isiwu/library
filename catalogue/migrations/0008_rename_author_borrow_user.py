# Generated by Django 4.0.8 on 2022-12-10 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_alter_borrow_ordered_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrow',
            old_name='author',
            new_name='user',
        ),
    ]
