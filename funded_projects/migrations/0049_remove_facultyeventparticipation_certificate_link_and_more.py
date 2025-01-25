# Generated by Django 5.1 on 2024-08-11 06:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funded_projects', '0048_remove_guestlecture_certificate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultyeventparticipation',
            name='certificate_link',
        ),
        migrations.RemoveField(
            model_name='facultyeventparticipation',
            name='date',
        ),
        migrations.RemoveField(
            model_name='facultyeventparticipation',
            name='faculty_name',
        ),
        migrations.RemoveField(
            model_name='facultyeventparticipation',
            name='program_nature',
        ),
        migrations.RemoveField(
            model_name='facultyeventparticipation',
            name='sponsoring_agencies',
        ),
        migrations.AddField(
            model_name='facultyeventparticipation',
            name='date_from',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='facultyeventparticipation',
            name='date_to',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='facultyeventparticipation',
            name='event_type',
            field=models.CharField(choices=[('FDP', 'FDP'), ('Workshop', 'Workshop'), ('Seminar', 'Seminar'), ('Conference', 'Conference')], default='FDP', max_length=20),
        ),
        migrations.AddField(
            model_name='facultyeventparticipation',
            name='mode',
            field=models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], default='Offline', max_length=10),
        ),
        migrations.AddField(
            model_name='facultyeventparticipation',
            name='report_certificate',
            field=models.FileField(blank=True, null=True, upload_to='faculty_event_reports/'),
        ),
        migrations.AddField(
            model_name='facultyeventparticipation',
            name='sponsoring_agency',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='facultyeventparticipation',
            name='program_title',
            field=models.CharField(default='', max_length=300),
        ),
    ]
