from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    # The two print statements were written by me only for 
    # testing reasons. I wanted to check the exact content of the 
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
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)