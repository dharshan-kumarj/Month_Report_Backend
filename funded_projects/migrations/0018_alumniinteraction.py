# Generated by Django 5.0.7 on 2024-08-05 19:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funded_projects', '0017_incomegeneratedprogram'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumniInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumni_name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('event_title', models.CharField(max_length=300)),
                ('event_date', models.DateField()),
                ('student_participants', models.PositiveIntegerField()),
                ('report_link', models.URLField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alumni_interactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
