from django.shortcuts import render, redirect
from .forms import EmploymentForm



def employment_view(request):
    if request.method == 'POST': 
        form = EmploymentForm(request.POST, request.FILES)
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)
        if form.is_valid():
            form.save()
            print("Form saved successfully!")
            return redirect('employment:employment')
        else:
            print("Form errors:", form.errors)
    else:
        form = EmploymentForm()
    return render(request, 'employment/career.html', {'form': form}) 

