# Generated by Django 4.0.7 on 2023-03-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_patient_lungs_re'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_kidney_re',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('creatinine', models.CharField(max_length=255)),
                ('bun', models.CharField(max_length=255)),
                ('urine_albumin', models.CharField(max_length=255)),
                ('urine_protien', models.CharField(max_length=255)),
                ('serum_creatinine', models.CharField(max_length=255)),
                ('urine_output', models.CharField(max_length=255)),
                ('urinalysis', models.CharField(max_length=255)),
                ('rbc', models.CharField(max_length=255)),
                ('kidney_biopsy', models.CharField(max_length=255)),
                ('immunological', models.CharField(max_length=255)),
                ('blood_type', models.CharField(max_length=255)),
                ('tissue_type', models.CharField(max_length=255)),
                ('cross_test', models.CharField(max_length=255)),
                ('imaging', models.CharField(max_length=255)),
                ('viral_test', models.CharField(max_length=255)),
            ],
        ),
    ]
