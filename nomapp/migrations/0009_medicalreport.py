# Generated by Django 4.2.7 on 2023-11-29 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomapp', '0008_alter_doctoravailability_clinic_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField()),
                ('symptoms', models.TextField()),
                ('diagnosis', models.TextField()),
                ('treatment', models.TextField()),
                ('comments', models.TextField(blank=True, null=True)),
                ('is_reviewed', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generated_reports', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_reports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
