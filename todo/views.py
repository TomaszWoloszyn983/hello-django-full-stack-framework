from django.shortcuts import render, redirect
from .models import Item

# Create your views here.


def get_todo_list(request):
    # Two print statements are written by me only for 
    # testing reasons. I watend to check the exact content of the 
    # items and the context variables.
    items = Item.objects.all()
    context = {
        'items': items 
    }
    for item in items:
        print(f"Print items: {item}")

    print(f'Print dictionary: {context}')
    # return HttpResponse()
    return render(request, "todo/todo_list.html", context)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')