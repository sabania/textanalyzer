# Generated by Django 2.0.5 on 2018-07-02 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfanalyzer', '0019_uploadfile_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='session_key',
            field=models.CharField(blank=True, default='0000', max_length=40),
        ),
    ]