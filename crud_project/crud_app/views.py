# from django.shortcuts import render

# Create your views here.
# crud_app/views.py

from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

items = {}  
def home(request):
    return render(request, './templates/home.html') 


def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = Item(len(items) + 1, form.cleaned_data['name'], form.cleaned_data['description'])
            items[item.id] = item
            return redirect('list_items')
    else:
        form = ItemForm()
    return render(request, 'create_item.html', {'form': form})

def list_items(request):
    return render(request, 'list_items.html', {'items': items.values()})

def delete_item(request, item_id):
    if request.method == 'POST':
        if item_id in items:
            del items[item_id]
            return redirect('list_items')
    return render(request, 'delete_item.html', {'item_id': item_id})

def edit_item(request, item_id):
    item = items.get(item_id)
    if not item:
        return redirect('list_items')

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    else:
        form = ItemForm(instance=item)
    
    return render(request, 'edit_item.html', {'form': form})
# Implement edit_item and delete_item views similarly
