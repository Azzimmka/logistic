# Generated by Django 5.1 on 2024-09-02 16:24

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_license_pdf'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asia',
            options={'ordering': ('-created',), 'verbose_name': 'Asian Country', 'verbose_name_plural': 'Asian Countries'},
        ),
        migrations.AlterModelOptions(
            name='europe',
            options={'verbose_name': 'European Country', 'verbose_name_plural': 'European Countries'},
        ),
        migrations.RemoveField(
            model_name='asia',
            name='country',
        ),
        migrations.RemoveField(
            model_name='asia',
            name='discription',
        ),
        migrations.RemoveField(
            model_name='europe',
            name='country',
        ),
        migrations.RemoveField(
            model_name='europe',
            name='discription',
        ),
        migrations.AlterField(
            model_name='asia',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='asia_logos/'),
        ),
        migrations.AlterField(
            model_name='europe',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='europe_logos/'),
        ),
        migrations.CreateModel(
            name='AsiaTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('country', models.CharField(max_length=50, verbose_name='country')),
                ('description', models.TextField(verbose_name='description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='app.asia')),
            ],
            options={
                'verbose_name': 'Asian Country Translation',
                'db_table': 'app_asia_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='EuropeTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('country', models.CharField(max_length=50, verbose_name='country')),
                ('description', models.TextField(verbose_name='description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='app.europe')),
            ],
            options={
                'verbose_name': 'European Country Translation',
                'db_table': 'app_europe_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
