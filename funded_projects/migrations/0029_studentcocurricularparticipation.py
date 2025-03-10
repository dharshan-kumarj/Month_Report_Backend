# Generated by Django 5.0.7 on 2024-08-06 12:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funded_projects', '0028_studenteventparticipation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCoCurricularParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(help_text='Registration number of the student', max_length=50)),
                ('student_name', models.CharField(help_text='Name of the student', max_length=200)),
                ('activity', models.CharField(choices=[('NCC', 'NCC'), ('NSS', 'NSS'), ('NON_TECH', 'Non-Technical Event')], max_length=20)),
                ('host_institute_and_place', models.CharField(help_text='Host institute and place', max_length=300)),
                ('award', models.CharField(blank=True, help_text='Award received, if any', max_length=200, null=True)),
                ('certificate_link', models.URLField(help_text='Link to the certificate')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='co_curricular_participations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Student Co-Curricular Participations',
            },
        ),
    ]
