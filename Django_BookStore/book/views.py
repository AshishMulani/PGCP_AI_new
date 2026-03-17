from django.shortcuts import render

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

#def about(request):
