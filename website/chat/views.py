from django.shortcuts import render

# Create your views here.


def index(request):
    context = dict(title="chat")
    return render(request, "chat/index.html", context=context)


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
