# Generated by Django 2.2.4 on 2024-06-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_jobs',
            field=models.ManyToManyField(related_name='favorite_jobs', to='app1.Job'),
        ),
    ]