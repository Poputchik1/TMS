# Generated by Django 4.0.4 on 2022-05-31 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_attendance_info_in_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='attendance_info',
            new_name='attendance',
        ),
    ]