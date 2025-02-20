# Generated by Django 4.0.7 on 2023-03-06 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0010_liv_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='lungs_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=255)),
                ('donor_id', models.CharField(max_length=255)),
                ('fev', models.CharField(max_length=255)),
                ('chest_x_ray', models.CharField(max_length=255)),
                ('pef', models.CharField(max_length=255)),
                ('bpt', models.CharField(max_length=255)),
                ('blood_test', models.CharField(max_length=255)),
                ('tumor_size', models.CharField(max_length=255)),
                ('sputum_culture', models.CharField(max_length=255)),
                ('tst', models.CharField(max_length=255)),
                ('igras', models.CharField(max_length=255)),
                ('ct_scan', models.CharField(max_length=255)),
                ('mri_scan', models.CharField(max_length=255)),
                ('pet_scan', models.CharField(max_length=255)),
                ('blood_type', models.CharField(max_length=255)),
                ('tissue_typing', models.CharField(max_length=255)),
                ('crossmatch', models.CharField(max_length=255)),
                ('viral_test', models.CharField(max_length=255)),
            ],
        ),
    ]
