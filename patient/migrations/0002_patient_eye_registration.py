# Generated by Django 4.0.7 on 2023-03-07 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_eye_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('iop', models.CharField(max_length=255)),
                ('visual_acuity', models.CharField(max_length=255)),
                ('corneal_thickness', models.CharField(max_length=255)),
                ('corneal_topo', models.CharField(max_length=255)),
                ('tissue_type', models.CharField(max_length=255)),
                ('corneal_curvature', models.CharField(max_length=255)),
                ('corneal_dia', models.CharField(max_length=255)),
                ('endothelial', models.CharField(max_length=255)),
            ],
        ),
    ]
