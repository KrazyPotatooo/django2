# Generated by Django 5.0 on 2023-12-30 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0009_rename_date_added_date_added_deadline_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albums',
            old_name='durationID',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='albums',
            old_name='titleID',
            new_name='song_name',
        ),
    ]
