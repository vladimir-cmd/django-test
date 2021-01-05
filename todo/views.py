from django.shortcuts import render
from .models import Item


# Create your views here.
def love_ye(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
