# Generated by Django 2.2.4 on 2024-05-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_job_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='logo',
            field=models.ImageField(default=1, upload_to='logo/'),
            preserve_default=False,
        ),
    ]
