# Generated by Django 5.1 on 2024-09-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='licenses/'),
        ),
    ]
