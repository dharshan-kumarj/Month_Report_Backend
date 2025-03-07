# Generated by Django 5.1 on 2024-08-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funded_projects', '0053_alter_alumniinteraction_report_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placementhigherstudiesentrepreneurship',
            name='date',
        ),
        migrations.RemoveField(
            model_name='placementhigherstudiesentrepreneurship',
            name='faculty_designation',
        ),
        migrations.RemoveField(
            model_name='placementhigherstudiesentrepreneurship',
            name='faculty_name',
        ),
        migrations.RemoveField(
            model_name='placementhigherstudiesentrepreneurship',
            name='report_link',
        ),
        migrations.RemoveField(
            model_name='placementhigherstudiesentrepreneurship',
            name='resource_person_details',
        ),
        migrations.AddField(
            model_name='placementhigherstudiesentrepreneurship',
            name='date_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='placementhigherstudiesentrepreneurship',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='placementhigherstudiesentrepreneurship',
            name='report_certificate',
            field=models.FileField(blank=True, null=True, upload_to='images/faculty_mooc/'),
        ),
        migrations.AddField(
            model_name='placementhigherstudiesentrepreneurship',
            name='resource_person_company',
            field=models.CharField(blank=True, help_text='Company details', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='placementhigherstudiesentrepreneurship',
            name='resource_person_designation',
            field=models.CharField(blank=True, help_text='Designation/Organization details', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='placementhigherstudiesentrepreneurship',
            name='program_title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
