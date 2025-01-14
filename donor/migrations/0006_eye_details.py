# Generated by Django 4.0.7 on 2023-02-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0005_organ_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='eye_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=255)),
                ('donor_id', models.CharField(max_length=255)),
                ('tonometry', models.CharField(max_length=255)),
                ('slit_lamp', models.CharField(max_length=255)),
                ('pachymetry', models.CharField(max_length=255)),
                ('serological_testing', models.CharField(max_length=255)),
                ('culture', models.CharField(max_length=255)),
                ('microscopy', models.CharField(max_length=255)),
                ('tissue_type', models.CharField(max_length=255)),
                ('hla', models.CharField(max_length=255)),
                ('corneal_mes', models.CharField(max_length=255)),
                ('corneal_curv', models.CharField(max_length=255)),
                ('corneal_topo', models.CharField(max_length=255)),
                ('corneal_dia', models.CharField(max_length=255)),
                ('endothelial_cell', models.CharField(max_length=255)),
            ],
        ),
    ]
