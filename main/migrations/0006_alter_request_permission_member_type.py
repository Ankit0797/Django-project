# Generated by Django 3.2 on 2022-04-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_request_permission_revoke_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_permission',
            name='Member_type',
            field=models.CharField(choices=[('New Access', 'New Access'), ('Modify Access', 'Modify Access')], default='Incomplete', max_length=100),
        ),
    ]
