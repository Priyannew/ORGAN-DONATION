# Generated by Django 4.0.7 on 2023-03-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_delete_patient_heart_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_heart_re',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('ejection_fraction', models.CharField(max_length=255)),
                ('pap', models.CharField(max_length=255)),
                ('pvg', models.CharField(max_length=255)),
                ('aortic_valve', models.CharField(max_length=255)),
                ('lavi', models.CharField(max_length=255)),
                ('lvef', models.CharField(max_length=255)),
                ('mitral_valve_regurgitation', models.CharField(max_length=255)),
                ('mitral_valve_stenosis', models.CharField(max_length=255)),
                ('wall_motion', models.CharField(max_length=255)),
                ('qt_interval', models.CharField(max_length=255)),
                ('qrs_duration', models.CharField(max_length=255)),
                ('atrial', models.CharField(max_length=255)),
                ('bradycardia', models.CharField(max_length=255)),
                ('heart_rate', models.CharField(max_length=255)),
                ('p_wave', models.CharField(max_length=255)),
                ('pulmonary', models.CharField(max_length=255)),
                ('cardiac_o', models.CharField(max_length=255)),
                ('coronary_art', models.CharField(max_length=255)),
                ('coronary_ani', models.CharField(max_length=255)),
                ('mild_stenosis', models.CharField(max_length=255)),
                ('moderate_stenosis', models.CharField(max_length=255)),
                ('ffr', models.CharField(max_length=255)),
                ('stenosis', models.CharField(max_length=255)),
                ('heart_size', models.CharField(max_length=255)),
                ('hemo', models.CharField(max_length=255)),
                ('blood_type', models.CharField(max_length=255)),
                ('tissue_type', models.CharField(max_length=255)),
            ],
        ),
    ]
