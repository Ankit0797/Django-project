import datetime
from datetime import datetime
from dateutil import relativedelta
from django.db import models
# Create your models here.

class Employees(models.Model):
    GRADE = (
        ('MT', 'MT'),
        ('J1', 'J1'),
        ('J2', 'J2'),
        ('J3', 'J3'),
        ('J4', 'J4'),
        ('J5', 'J5'),
        ('J6', 'J6'),
        ('M1', 'M1'),
        ('M2', 'M2'),
        ('M3', 'M3'),
        ('M4', 'M4'),
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
    )
    STATUS = (('Active','Active'),
    ('InActive','InActive'))
    Empid = models.CharField(max_length=100,blank=True, help_text="<br>Use only capital INT") 
    Employee_name = models.CharField(max_length=100,blank=True)
    Join_Date = models.DateField(help_text = "Please use the following format: <em>YYYY-MM-DD</em>.") 
    Grade = models.CharField(max_length=100, choices=GRADE)
    Skill = models.TextField(default=None, blank= True) 
    Certified_Skill = models.TextField(default=None, blank= True) 
    Experience = models.CharField(max_length=100, default=None,blank= True, help_text="<br>Type Experience in number.<br> Format: Year:YY, Months:MM ") 
    KRA = models.TextField(default=None, blank= True) 
    Annual_CTC = models.FloatField(default=0, help_text="<br>Type entire number i.e, 3lacs: 300000<br>Do not add comma in between numbers.") 
    Month_Salary = models.IntegerField(default=0, help_text="<br>just type Any number: '1','2','3'<br> After saving Month Salary will be calculate") 
    def save(self, *args, **kwargs):
            self.Month_Salary= self.Annual_CTC/12
            super(Employees, self).save(*args, **kwargs)
    CV = models.FileField(upload_to='files',blank= True, help_text="ONLY .PDF files are ALLOWED!.<br>Size limit of file is 2MB")
    status = models.CharField(max_length=100, choices=STATUS, default='CHOOSE')
    
    # history = HistoricalRecords()

    def __str__(self):
        return self.Empid 
    
class Add_Project(models.Model):
    STATUS = (('Active','Active'),
    ('InActive','InActive'))
    Project_name = models.CharField(max_length=100,blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default='CHOOSE')
    # history = HistoricalRecords()
    
    def __str__(self):
        return self.Project_name
    
class Project(models.Model):
    STATUS = (('Active','Active'),
    ('InActive','InActive'))
    PAY_CYCLE = (('Monthly','Monthly'),
    ('Quarterly','Quarterly'),
    ('Half Yearly','Half Yearly'),
    ('Yearly','Yearly'),
    ('Partially','Partially'))
    RATE = (('Resource wise','Resource wise'),
            ('Man Hours','Man Hours'),
            ('Man Days','Man Days'))
    Project_name = models.ForeignKey(Add_Project, on_delete=models.CASCADE, blank=True, help_text = "<br>EDIT: select project name and click pencil symbol.<br>ADD: Click plus symbol.")
    Project_Start_Date = models.DateTimeField(help_text = "Please use the following format: <em>YYYY-MM-DD</em><br> Time: <em>00:00:00</em>") 
    Project_End_Date = models.DateTimeField(help_text = "Please use the following format: <em>YYYY-MM-DD</em><br> Time: <em>00:00:00</em>")
    def save(self, *args, **kwargs):
        self.Duration = self.Project_Start_Date - self.Project_End_Date
        super(Project, self).save(*args, **kwargs)
    Duration = models.CharField(max_length=100, help_text = "<br>just type Any number: '1','2','3'<br> After saving Duration will be calculate")
    PO_Number = models.CharField(max_length=100)  
    PO_Date = models.DateField(help_text = "<br>Please use the following format: <em>YYYY-MM-DD</em>.") 
    SOW = models.TextField(blank= True) 
    PO_Terms_and_Conditions = models.TextField(blank= True) 
    Payment_Cycle = models.CharField(max_length=100, choices=PAY_CYCLE, blank= True)
    Compliance_document = models.TextField(blank= True) 
    Rate_Type = models.CharField(max_length=100, choices=RATE)
    Empid = models.ForeignKey(Employees, on_delete=models.CASCADE, help_text = "<br>EDIT: select Empid and click pencil symbol.<br>ADD: Click plus symbol.") 
    status = models.CharField(max_length=100, choices=STATUS)
    # history = HistoricalRecords()
    
    def __str__(self):
        return self.PO_Number 
    
class Payment(models.Model):
    STATUS = (('Invoice Not Submitted','Invoice Not Submitted'),
              ('Payment Pending','Payment Pending'),
              ('Invoice Submitted','Invoice Submitted'),
              ('Payment Received','Payment Received'))
    PAY_CYCLE = (('Monthly','Monthly'),
    ('Quarterly','Quarterly'),
    ('Half Yearly','Half Yearly'),
    ('Yearly','Yearly'),
    ('Partially','Partially'))
    # Duration = models.CharField(max_length=100) 
    PO_Number = models.ForeignKey(Project, on_delete=models.CASCADE, help_text = "<br>EDIT: select project number and click pencil symbol.<br>ADD: Click plus symbol.") 
    Project_name = models.ForeignKey(Add_Project, on_delete=models.CASCADE, blank=True, help_text = "<br>EDIT: select project name and click pencil symbol.<br>ADD: Click plus symbol.")
    Compliance = models.FileField(upload_to='files', help_text="ONLY .PDF files are ALLOWED!.<br>Size limit of file is 2MB")
    Rate_From_Client = models.CharField(max_length=100,  help_text="<br>Type entire number i.e, 3lacs: 300000") 
    Billing_Date = models.DateField(help_text = "<br>Please use the following format: <em>YYYY-MM-DD</em>.") 
    Payment_Cycle = models.CharField(max_length=100, choices=PAY_CYCLE)
    def save(self, *args, **kwargs):
        a=self.Payment_Cycle
        my_string1 = str(self.Billing_Date)
        start = datetime.strptime(my_string1, "%Y-%m-%d")
        if a=='Monthly':
            # for n in range(1,12):
                start = start + relativedelta.relativedelta(months=1)
                self.Billing_Cycle= start
                print(self.Billing_Cycle)
        elif a=='Quarterly':
            # for n in range(1,4):
                start = start + relativedelta.relativedelta(months=3)
                self.Billing_Cycle= start
                print(self.Billing_Cycle)
        elif a=='Half Yearly':
            # for n in range(1,2):
                start = start + relativedelta.relativedelta(months=6)
                self.Billing_Cycle= start
                print(self.Billing_Cycle)
        elif a=='Yearly':
            # for n in range(1,2):
                start = start + relativedelta.relativedelta(months=12)
                self.Billing_Cycle= start
                print(self.Billing_Cycle)
        elif a=='Partially':
            # for n in range(1,2):
                self.Billing_Cycle= "None"
                print(self.Billing_Cycle)
        else:
            print('enter valid name')
        super(Payment, self).save(*args, **kwargs)
    Billing_Cycle = models.CharField(max_length=100, default='0')
    Partial_Cycle= models.CharField(max_length=100, default='None', blank= True, help_text="ONLY TYPE IN WHEN PAYMENT CYCLE IS PARTIALLY or else leave it blank")
    Payment_Status = models.CharField(max_length=100, choices=STATUS, default='0')
    Document_Submitted = models.BooleanField(default=False)
    # history = HistoricalRecords()
    

class Request_Permission(models.Model):
    Member_type = (('New Access','New Access'),
    ('Modify Access','Modify Access'))
    STATUS = (('Approved','Approved'),
              ('Rejected','Rejected'),
    ('Task pending','Task pending'))
    Employee_Department = (('Finance','Finance'),
              ('PMO','PMO'),
    ('HR','HR'))
    Empid = models.CharField(max_length=100,blank=True, help_text="<br>Use only capital INT") 
    Employee_name = models.CharField(max_length=100,blank=True)
    Employee_Designation = models.CharField(max_length=100,blank=True)
    Employee_Department = models.CharField(max_length=100, choices=Employee_Department, default='Choose')
    Member_type = models.CharField(max_length=100, choices=Member_type, default='Member type')
    Read = models.BooleanField(default=False)
    Read_Write = models.BooleanField(default=False)
    Admin = models.BooleanField(default=False)    
    status = models.CharField(max_length=100, choices=STATUS, default='Task pending', help_text="<br>Only APPROVED by Admin<br><strong>CAUTION</strong>: If Admin see's this APPROVED<br>then he will not open this file")
    
    # history = HistoricalRecords()
    
class Revoke_Permission(models.Model):
    STATUS = (('Approved','Approved'),
              ('Rejected','Rejected'),
    ('Task pending','Task pending'))
    Employee_Department = (('Finance','Finance'),
              ('PMO','PMO'),
    ('HR','HR'))
    Empid = models.CharField(max_length=100,blank=True, help_text="<br>Use only capital INT") 
    Employee_name = models.CharField(max_length=100,blank=True)
    Employee_Designation = models.CharField(max_length=100,blank=True)
    Employee_Department = models.CharField(max_length=100, choices=Employee_Department, default='Choose')
    status = models.CharField(max_length=100, choices=STATUS, default='Task pending', help_text="<br>Only APPROVED by Admin<br><strong>CAUTION</strong>: If Admin see's this APPROVED<br>then he will not open this file")
    
    # history = HistoricalRecords()
 