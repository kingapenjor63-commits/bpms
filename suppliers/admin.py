from django.contrib import admin
from .models import Department, CompanyContact

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    search_fields = ['name']
    ordering = ['name']

@admin.register(CompanyContact)
class CompanyContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'contact_person_name', 'department', 'country', 'email_id', 'created_at']
    search_fields = ['company_name', 'contact_person_name', 'email_id', 'country']
    list_filter = ['department', 'country', 'created_at']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 50