# Generated by Django 2.0.5 on 2018-07-05 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfanalyzer', '0020_auto_20180702_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='adjective_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='noun_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='verb_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]