from django.shortcuts import render


def employment_view(request):
    return render(request, 'employment/career.html') 