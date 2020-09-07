from django.shortcuts import render

# Create your views here.

def chat(request):
    context = dict(title="chat")
    return render(request, 'chat/chat.html', context=context)
