from django.core.management.base import BaseCommand
from suppliers.models import Department

DEPARTMENTS = [
    'Anaesthesia',
    'Surgery',
    'Traditional Medicines',
    'RCDC',
    'Radiology',
    'Psychiatry',
    'Physiotherapy',
    'Pharmacy',
    'Operation Theatre',
    'Orthopedic',
    'Ophthalmology',
    'Medical',
    'Paediatric',
    'Laboratory',
    'Intensive Care Unit',
    'Hemodialysis',
    'Gynaecology',
    'General Equipment',
    'Forensic',
    'ENT',
    'Dermatology',
    'CSSD',
    'Chemotheraphy',
    'Dental',
    'Dermatology Gloderm',
]

class Command(BaseCommand):
    help = 'Load all departments into the database'

    def handle(self, *args, **kwargs):
        for dept_name in DEPARTMENTS:
            dept, created = Department.objects.get_or_create(name=dept_name)
            if created:
                self.stdout.write(f'✅ Created: {dept_name}')
            else:
                self.stdout.write(f'⏭️ Already exists: {dept_name}')
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Total departments: {Department.objects.count()}'))