# Generated by Django 2.0.5 on 2018-06-22 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdfanalyzer', '0006_uploadfile_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='file_name',
        ),
    ]