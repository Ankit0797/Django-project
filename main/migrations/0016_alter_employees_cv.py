# Generated by Django 3.2 on 2022-04-12 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20220412_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='CV',
            field=models.FileField(blank=True, help_text='ONLY .PDF files are ALLOWED!.<br>Size limit of file is 2MB', upload_to='files'),
        ),
    ]
