# Generated by Django 5.1.4 on 2025-02-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Engineer', 'Engineer')], max_length=10, null=True),
        ),
    ]
