# Generated by Django 4.0.7 on 2023-03-15 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0020_heart_details_approved_kid_reg_approved_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liv_reg',
            old_name='tissue_typing',
            new_name='tissue_type',
        ),
        migrations.RenameField(
            model_name='lun_reg',
            old_name='tissue_typing',
            new_name='tissue_type',
        ),
    ]
