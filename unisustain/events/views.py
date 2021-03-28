from django.shortcuts import render

# Create your views here.
# Create your views here.
from .models import Event

def get_all_events(request):
    all_events = Event.objects.all()
    context = {
        'all_events':all_events
    }
    return render(request, "events/all_events.html", context)

def get_event(request, event_id):
    event = Event.objects.get(eventID = event_id)
    context = {
        'event':event
    }
    return render(request, "events/event_view.html", context)

def create_event(response):
    if response.method == "POST":
        print("hello")
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