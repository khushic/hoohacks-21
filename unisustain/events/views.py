from django.shortcuts import render, redirect

# Create your views here.
from .models import Event
from django.forms.models import model_to_dict


def get_all_events(request):
    all_events = list(Event.objects.all().values())
    print(all_events)
    for i in all_events:
        i["tags"] = i["tags"].split(", ")
    context = {
        'all_events':all_events
    }
    return render(request, "events/all_events.html", context)

def get_event(request, event_id):
    query = Event.objects.get(eventID = event_id)
    event = model_to_dict(query)
    event["tags"] = event["tags"].split(", ")
    context = {
        'event':event
    }
    return render(request, "events/event_view.html", context)

def create_event(response):
    if response.method == "POST":
        created_obj = Event.objects.get_or_create(
            eventname=response.POST.get('event_name'),
            eventdate=response.POST.get('event_date'),
            tags=response.POST.get('tags'),
            school=response.POST.get('schools'),
            description=response.POST.get('description'),
            info=response.POST.get('info'),
            applink=response.POST.get('apply'),
        )
    return redirect("../")
