# Generated by Django 5.1 on 2024-08-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funded_projects', '0037_remove_internationalinternship_certificate_photos_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentseedmoney',
            old_name='faculty_name',
            new_name='reg_no',
        ),
        migrations.RemoveField(
            model_name='studentseedmoney',
            name='proof_link',
        ),
        migrations.AddField(
            model_name='studentseedmoney',
            name='proof',
            field=models.FileField(blank=True, null=True, upload_to='images/conference_proofs/'),
        ),
    ]
