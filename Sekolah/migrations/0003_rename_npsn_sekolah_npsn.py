# Generated by Django 4.1.5 on 2023-01-20 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sekolah', '0002_sekolah_create_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sekolah',
            old_name='npsn',
            new_name='NPSN',
        ),
    ]
