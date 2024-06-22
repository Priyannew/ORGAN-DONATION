# Generated by Django 4.0.7 on 2023-02-22 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_rename_donor_donor_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='enroll_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('dod', models.DateField()),
                ('height', models.CharField(max_length=255)),
                ('weight', models.CharField(max_length=255)),
                ('martial_status', models.CharField(max_length=255)),
                ('cause_of_death', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
