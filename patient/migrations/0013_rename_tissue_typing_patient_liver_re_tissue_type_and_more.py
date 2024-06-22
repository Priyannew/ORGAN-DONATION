# Generated by Django 4.0.7 on 2023-03-15 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0012_patient_eye_registration_approved_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient_liver_re',
            old_name='tissue_typing',
            new_name='tissue_type',
        ),
        migrations.RenameField(
            model_name='patient_lungs_re',
            old_name='tissue_typing',
            new_name='tissue_type',
        ),
    ]
