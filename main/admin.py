from django.contrib import admin
from .models import Employees, Add_Project, Project, Payment, Request_Permission, Revoke_Permission

class EmpAdmin(admin.ModelAdmin):
    list_display=('Empid','Employee_name','Join_Date','KRA','Month_Salary','status')
    list_editable=()
    list_per_page=10
    search_fields=['Empid','Employee_name']
    list_filter=['status','Join_Date']
    date_hierarchy = 'Join_Date'
admin.site.register(Employees, EmpAdmin)

class AddAdmin(admin.ModelAdmin):
    list_display=['Project_name','status']
    list_editable=()
    list_per_page=10
    search_fields=['Project_name']
    list_filter=['status']
admin.site.register(Add_Project, AddAdmin)

class ProAdmin(admin.ModelAdmin):
    @admin.display(description='Project_Start_Date')
    def admin_Start(self, obj):
        return obj.Project_Start_Date.strftime('%Y-%m-%d')
    @admin.display(description='Project_End_Date')
    def admin_End(self, obj):
        return obj.Project_End_Date.strftime('%Y-%m-%d')
    list_display=['Project_name','Empid','admin_Start','admin_End','Duration','Payment_Cycle','status']
    list_editable=()
    list_per_page=10
    search_fields=['Empid__Empid','Project_name__Project_name']
    list_filter=['status','Payment_Cycle']
    date_hierarchy = 'Project_Start_Date'
    # raw_id_fields = ["Project_Selected","Empid"]
admin.site.register(Project, ProAdmin)

class PAdmin(admin.ModelAdmin):
    list_display=['Project_name','PO_Number','Payment_Cycle','Billing_Date','Billing_Cycle','Partial_Cycle','Payment_Status','Document_Submitted']
    list_editable=['Billing_Date']
    list_per_page=10
    search_fields=['PO_Number__PO_Number','Project_name__Project_name']
    list_filter=['Payment_Status','Payment_Cycle','Document_Submitted']
    date_hierarchy = 'Billing_Date'
admin.site.register(Payment, PAdmin)

class Request_PermissionAdmin(admin.ModelAdmin):
    list_display=['Empid','Employee_name','Member_type','Read','Read_Write','Admin','status']
    list_editable=['status']
    list_per_page=10
    search_fields=['Empid','Employee_name','Member_type']
    list_filter=['Read','Read_Write','Admin','status']
admin.site.register(Request_Permission, Request_PermissionAdmin)

class Revoke_PermissionAdmin(admin.ModelAdmin):
    list_display=['Empid','Employee_name','Employee_Designation','Employee_Department','status']
    list_editable=['status']
    list_per_page=10
    search_fields=['Empid','Employee_name','Employee_Department']
    list_filter=['status']
admin.site.register(Revoke_Permission, Revoke_PermissionAdmin)


admin.site.site_header = "IDBI INTECH"
admin.site.site_title = "IDBI INTECH Portal"
admin.site.index_title = "Welcome to IDBI INTECH Portal"