# Generated by Django 4.0.7 on 2023-02-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0004_alter_enroll_details_dob_alter_enroll_details_dod'),
    ]

    operations = [
        migrations.CreateModel(
            name='organ_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.BigIntegerField()),
                ('email', models.CharField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('gender', models.CharField(max_length=255)),
                ('aadhaar_no', models.BigIntegerField()),
                ('cause_of_death', models.CharField(max_length=255)),
                ('blood', models.CharField(max_length=255)),
                ('organ_name', models.CharField(max_length=255)),
                ('f_consent', models.CharField(max_length=255)),
                ('dod', models.DateField()),
                ('medical_conditions', models.CharField(max_length=255)),
                ('general_appearance', models.CharField(max_length=255)),
                ('cardi_exam', models.CharField(max_length=255)),
                ('respiratory_health', models.CharField(max_length=255)),
                ('liver_function', models.CharField(max_length=255)),
                ('renal_function', models.CharField(max_length=255)),
                ('drug_usage', models.CharField(max_length=255)),
                ('organ_function', models.CharField(max_length=255)),
                ('cold_ischemia', models.CharField(max_length=255)),
                ('ecg', models.CharField(max_length=255)),
                ('biopsy', models.CharField(max_length=255)),
                ('imaging_test', models.CharField(max_length=255)),
                ('visual_acuity', models.CharField(max_length=255)),
            ],
        ),
    ]