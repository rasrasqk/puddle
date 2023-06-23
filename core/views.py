from django.shortcuts import render , redirect
from item.models import Category, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_solid=False)[:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories
    })



def contact(request):
    # Logic for handling contact page
    return render(request, 'core/contact.html')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')

    else:   
        form = SignupForm()


    return render(request, 'core/signup.html',{
        'form': form
    })

