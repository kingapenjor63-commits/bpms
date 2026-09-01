from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CompanyContactForm
from .models import CompanyContact

def portal_home(request):
    """Main portal page with form"""
    if request.method == 'POST':
        form = CompanyContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Your information has been submitted successfully!')
            return redirect('suppliers:portal_home')
    else:
        form = CompanyContactForm()
    
    # Get recent submissions
    recent_submissions = CompanyContact.objects.all()[:10]
    
    context = {
        'form': form,
        'recent_submissions': recent_submissions,
    }
    return render(request, 'suppliers/home.html', context)