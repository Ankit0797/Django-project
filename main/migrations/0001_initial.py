# Generated by Django 3.2 on 2022-04-03 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_name', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('InActive', 'InActive')], default='CHOOSE', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empid', models.CharField(blank=True, help_text='<br>Use only capital INT', max_length=100)),
                ('Employee_name', models.CharField(blank=True, max_length=100)),
                ('Join_Date', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('Grade', models.CharField(choices=[('MT', 'MT'), ('J1', 'J1'), ('J2', 'J2'), ('J3', 'J3'), ('J4', 'J4'), ('J5', 'J5'), ('J6', 'J6'), ('M1', 'M1'), ('M2', 'M2'), ('M3', 'M3'), ('M4', 'M4'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3')], max_length=100)),
                ('Skill', models.TextField()),
                ('Certified_Skill', models.TextField()),
                ('Experience', models.TextField(help_text='Type Experience in number.')),
                ('KRA', models.TextField()),
                ('Annual_CTC', models.FloatField(default=0, help_text='<br>Type entire number i.e, 3lacs: 300000<br>Do not add comma in between numbers.')),
                ('Month_Salary', models.IntegerField(default=0, help_text="<br>just type Any number: '1','2','3'<br> After saving Month Salary will be calculate")),
                ('CV', models.FileField(help_text='ONLY .PDF files are ALLOWED!.<br>Size limit of file is 2MB', upload_to='files')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('InActive', 'InActive')], default='CHOOSE', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Start_Date', models.DateTimeField(help_text='Please use the following format: <em>YYYY-MM-DD</em><br> Time: <em>00:00:00</em>')),
                ('Project_End_Date', models.DateTimeField(help_text='Please use the following format: <em>YYYY-MM-DD</em><br> Time: <em>00:00:00</em>')),
                ('Duration', models.CharField(help_text="<br>just type Any number: '1','2','3'<br> After saving Duration will be calculate", max_length=100)),
                ('PO_Number', models.CharField(max_length=100)),
                ('PO_Date', models.DateField(help_text='<br>Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('SOW', models.TextField()),
                ('PO_Terms_and_Conditions', models.TextField()),
                ('Payment_Cycle', models.CharField(choices=[('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Half Yearly', 'Half Yearly'), ('Yearly', 'Yearly'), ('Partially', 'Partially')], max_length=100)),
                ('Compliance_document', models.TextField()),
                ('Rate_Type', models.CharField(choices=[('Resource wise', 'Resource wise'), ('Man Hours', 'Man Hours'), ('Man Days', 'Man Days')], max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('InActive', 'InActive')], max_length=100)),
                ('Empid', models.ForeignKey(help_text='<br>EDIT: select Empid and click pencil symbol.<br>ADD: Click plus symbol.', on_delete=django.db.models.deletion.CASCADE, to='main.employees')),
                ('Project_name', models.ForeignKey(blank=True, help_text='<br>EDIT: select project name and click pencil symbol.<br>ADD: Click plus symbol.', on_delete=django.db.models.deletion.CASCADE, to='main.add_project')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Compliance', models.FileField(help_text='ONLY .PDF files are ALLOWED!.<br>Size limit of file is 2MB', upload_to='files')),
                ('Rate_From_Client', models.CharField(help_text='<br>Type entire number i.e, 3lacs: 300000', max_length=100)),
                ('Billing_Date', models.DateField(help_text='<br>Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('Billing_Cycle', models.DateField(help_text='<br>Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('Payment_Cycle', models.CharField(choices=[('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Half Yearly', 'Half Yearly'), ('Yearly', 'Yearly'), ('Partially', 'Partially')], max_length=100)),
                ('Payment_Status', models.CharField(choices=[('Not Submitted', 'Not Submitted'), ('Pending', 'Pending'), ('Submitted', 'Submitted'), ('Received', 'Received')], default='0', max_length=100)),
                ('Document_Submitted', models.BooleanField(default=False)),
                ('PO_Number', models.ForeignKey(help_text='<br>EDIT: select project number and click pencil symbol.<br>ADD: Click plus symbol.', on_delete=django.db.models.deletion.CASCADE, to='main.project')),
                ('Project_name', models.ForeignKey(blank=True, help_text='<br>EDIT: select project name and click pencil symbol.<br>ADD: Click plus symbol.', on_delete=django.db.models.deletion.CASCADE, to='main.add_project')),
            ],
        ),
    ]
