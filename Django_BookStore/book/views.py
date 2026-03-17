from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect

from .models import Book


# books=[{
#         'title':'python 3',
#         'author':'abc',
#         'price':900
#         },
#        {
#         'title': 'Data science',
#         'author': 'pqr',
#         'price': 1200
#        },
#        {
#         'title': 'java',
#         'author': 'xyz',
#         'price': 1000
#        }
#        ]


def home(request):
    books=Book.objects.all()
    context={'books':books}   #dict
    return render(request, 'book/home.html',context=context)

def about(request):
    return render(request, 'book/about.html',{'title':'About'})

def book_details(request,book_id):
    book=get_object_or_404(Book, id=book_id)
    return render(request, 'book/book_details.html', context={'book':book})

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('book-home')

    else:
        form=UserCreationForm()
        return render(request, 'book/register.html', {'title':'Register', 'form':form})

