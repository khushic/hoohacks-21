from django.shortcuts import render, redirect

from .models import Fund
from django.forms.models import model_to_dict

def get_all_grants(request):
    all_grants = list(Fund.objects.all().values())
    for i in all_grants:
        i["tags"] = i["tags"].split(", ")
    context = {
        'all_grants':all_grants
    }
    return render(request, "grants/all_grants.html", context)


def get_grant(request, grant_id):
    query = Fund.objects.get(fundID = grant_id)
    grant = model_to_dict(query)
    grant["tags"] = grant["tags"].split(", ")
    context = {
        'fund':grant
    }
    return render(request, "grants/grant_view.html", context)

def create_grant(response):
    if response.method == "POST":
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
