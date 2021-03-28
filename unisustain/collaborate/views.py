from django.shortcuts import render
from _datetime import datetime

from .models import Chat

# Create your views here.

def index(request):
    return render(request, 'collaborate/index.html')

def room(request, room_name):
    # if request.method == "POST":
        # created_obj = Chat.objects.create(
        #     id=request.user.id,
        #     username=request.user.username,
        #     message=request.POST.get('message'),
        #     time=datetime.now()
        # )
    chat = Chat()
    chat.id = request.user.id
    chat.username = request.user.username
    chat.message = request.user,
    chat.time = datetime.now()
    chat.save()
    return render(request, 'collaborate/room.html', {
        'room_name': room_name, 'username': request.user.username
    })