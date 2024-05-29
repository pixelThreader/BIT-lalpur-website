# Generated by Django 5.0.6 on 2024-05-28 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('facultyID', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('about', models.CharField(max_length=2000)),
                ('department', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('joined_on', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=1000)),
                ('localhost', models.CharField(max_length=255)),
                ('phone1', models.CharField(max_length=255)),
                ('phone_office', models.CharField(max_length=255)),
                ('faculty_email', models.CharField(max_length=500)),
                ('teaching_year', models.CharField(max_length=255)),
                ('research_year', models.CharField(max_length=255)),
                ('research_area', models.TextField()),
                ('publications', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='uploads/faculty_profile/')),
            ],
            options={
                'verbose_name': 'faculty',
                'verbose_name_plural': 'faculty',
            },
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2000)),
                ('uptime', models.DateTimeField(auto_now_add=True)),
                ('notificationID', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
            },
        ),
    ]