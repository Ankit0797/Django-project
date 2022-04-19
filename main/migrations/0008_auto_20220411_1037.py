# Generated by Django 3.2 on 2022-04-11 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220407_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_permission',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Task pending', 'Task pending')], default='Task pending', help_text="<br>Only APPROVED by Admin<br>If Admin see's this APPROVED<br>then he will not open this file", max_length=100),
        ),
        migrations.AlterField(
            model_name='revoke_permission',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Task pending', 'Task pending')], default='Task pending', help_text="<br>Only APPROVED by Admin<br>If Admin see's this APPROVED<br>then he will not open this file", max_length=100),
        ),
    ]
