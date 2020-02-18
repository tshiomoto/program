from django.shortcuts import render
from .models import Item, Person

# Create your views here.
def purchase(request):
    item_list = Item.objects.order_by('-item_name')[:1]
    person_list = Person.objects.order_by('-person_name')[:1]
    context = {
        "item_list": item_list,
        "person_list": person_list,
    }
    return render(request, 'test_moneys/purchase.html', context)