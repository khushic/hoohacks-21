from django.shortcuts import render

from .models import Fund

def get_all_grants(request):
    all_grants = Fund.objects.all()
    context = {
        'all_funds':all_grants
    }
    return render(request, "grants/all_grants.html", context)

def get_grant(request, grant_id):
    all_grants = Fund.objects.get(fundID = grant_id)
    context = {
        'all_funds':all_grants
    }
    return render(request, "grants/all_grants.html", context)
"""def get_grant(request):
    return render(request, "grants/temp.html")"""
