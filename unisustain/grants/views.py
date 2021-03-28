from django.shortcuts import render, redirect

from .models import Fund

def get_all_grants(request):
    all_grants = Fund.objects.all()
    context = {
        'all_funds':all_grants
    }
    return render(request, "grants/all_grants.html", context)

def get_grant(request, grant_id):
    grant = Fund.objects.get(fundID = grant_id)
    context = {
        'fund':grant
    }
    return render(request, "grants/grant_view.html", context)

def create_grant(response):
    if response.method == "POST":
        print("hello")
        created_obj = Fund.objects.get_or_create(
            fundname=response.POST.get('fund_name'),
            sponsor=response.POST.get('sponsor'),
            tags=response.POST.get('tags'),
            school=response.POST.get('schools'),
            description=response.POST.get('description'),
            info=response.POST.get('info'),
            applink=response.POST.get('apply'),
        )
    return redirect("../")
