from django.shortcuts import render

# Create your views here.
def touch_typing(request):
    context = dict(title="touch typing")
    return render(request, 'touch-typing/touch-typing.html', context=context)