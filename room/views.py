import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Room

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    try:
        room = Room.objects.get(slug=slug)
    except Room.DoesNotExist:
        raise Http404("Room not found")
    

    room_slug_json = json.dumps(room.slug)
    
    return render(request, 'room/room.html', {'room': room, 'room_slug_json': room_slug_json})
