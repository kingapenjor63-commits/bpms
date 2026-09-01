from django.db import models

class Department(models.Model):
    """All departments from the BoQ file"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class CompanyContact(models.Model):
    """Main model for storing company/contact information"""
    
    # Company Information
    company_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    
    # Contact Person
    contact_person_name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=20)
    email_id = models.EmailField()
    
    # Department (Foreign Key to Department model)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='contacts'
    )
    
    # Additional Information
    remarks = models.TextField(blank=True, null=True)
    
    # Tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.company_name} - {self.contact_person_name}"