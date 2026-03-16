from flask import render_template, redirect, url_for

from . import app
from .forms import RegistrationForm
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

@app.route('/')   #Decorator
def home():
    #return "<p>Hello World!</p>"
    books=Book.query.all()
    return(render_template('home.html',books=books))

@app.route('/about')
def about():
    return(render_template('about.html',title='About Us'))

@app.route('/book/<int:book_id>')   #Decorator
def book_details(book_id):
    book=Book.query.get_or_404(book_id)
    return(render_template('book_details.html',book=book))

@app.route('/register',methods=['GET','POST'])   #Decorator
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    else:
        print(form.errors)

    return(render_template('register.html',form=form, title='Register'))