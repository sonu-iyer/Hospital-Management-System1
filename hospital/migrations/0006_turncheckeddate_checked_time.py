# Generated by Django 4.1.4 on 2023-05-05 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_turncheckeddate_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='turncheckeddate',
            name='checked_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
