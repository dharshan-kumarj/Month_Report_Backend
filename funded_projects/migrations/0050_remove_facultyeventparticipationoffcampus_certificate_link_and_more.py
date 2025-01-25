# Generated by Django 5.1 on 2024-08-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funded_projects', '0049_remove_facultyeventparticipation_certificate_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultyeventparticipationoffcampus',
            name='certificate_link',
        ),
        migrations.RemoveField(
            model_name='facultyeventparticipationoffcampus',
            name='date',
        ),
        migrations.RemoveField(
            model_name='facultyeventparticipationoffcampus',
            name='faculty_name',
        ),
        migrations.RemoveField(
            model_name='facultyeventparticipationoffcampus',
            name='host_institution_place',
        ),
        migrations.RemoveField(
            model_name='facultyeventparticipationoffcampus',
            name='program_nature',
        ),
        migrations.RemoveField(
            model_name='facultyeventparticipationoffcampus',
            name='sponsoring_agencies',
        ),
        migrations.AddField(
            model_name='facultyeventparticipationoffcampus',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facultyeventparticipationoffcampus',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facultyeventparticipationoffcampus',
            name='date_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facultyeventparticipationoffcampus',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facultyeventparticipationoffcampus',
            name='event_type',
            field=models.CharField(choices=[('FDP', 'FDP'), ('Workshop', 'Workshop'), ('Seminar', 'Seminar'), ('Conference', 'Conference')], default='FDP', max_length=20),
        ),
        migrations.AddField(
            model_name='facultyeventparticipationoffcampus',
            name='host_institution',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='facultyeventparticipationoffcampus',
            name='mode',
            field=models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], default='Offline', max_length=10),
        ),
        migrations.AddField(
            model_name='facultyeventparticipationoffcampus',
            name='report_certificate',
            field=models.FileField(blank=True, null=True, upload_to='event_certificates/'),
        ),
        migrations.AddField(
            model_name='facultyeventparticipationoffcampus',
            name='sponsoring_agency',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='facultyeventparticipationoffcampus',
            name='program_title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
