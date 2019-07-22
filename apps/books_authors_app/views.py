from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author 
# Create your views here.
def index(request):
    print('the index method is running')
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'books_authors_app/index.html', context)

def add_book(request):
    print('the add book method is running')
    if request.method == "POST":
        val_from_title_field = request.POST["title"]
        val_from_desc_field = request.POST["desc"]
    Book.objects.create(title=val_from_title_field, desc=val_from_desc_field)
    return redirect('/')

def books(request, id):
    print('the book details method is running')
    this_book = Book.objects.get(id=id)
    context = {
        'this_book': Book.objects.get(id=id),
        'this_book_authors': this_book.authors.all(),
        'all_authors': Author.objects.all()
    }
    return render(request, 'books_authors_app/book_details.html', context)

def add_author_to_book(request, id):
    print('the add author to book method is running')
    print(request.POST)
    this_book = Book.objects.get(id=id)
    this_author = Author.objects.get(id=request.POST["author"])
    this_book.authors.add(this_author)
    print(this_author.first_name)
    return redirect('/')

def author_page(request):
    print('the author_page method is running')
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'books_authors_app/author.html', context)

def add_author(request):
    print('the add author method is running')
    if request.method == "POST":
        val_from_fname_field = request.POST["f_name"]
        val_from_lname_field = request.POST["l_name"]
        val_from_notes_field = request.POST["notes"]
    Author.objects.create(first_name=val_from_fname_field, last_name=val_from_lname_field, notes=val_from_notes_field)
    return redirect('/authors')

def authors(request, id):
    print('the author details method is running')
    this_author = Author.objects.get(id=id)
    context = {
        'this_author': Author.objects.get(id=id),
        'this_author_books': this_author.books.all(),
        'all_books': Book.objects.all()
    }
    return render(request, 'books_authors_app/author_details.html', context)

def add_book_to_author(request, id):
    print('the add book to author method is running')
    print(request.POST)
    this_author = Author.objects.get(id=id)
    this_book = Book.objects.get(id=request.POST["book"])
    this_author.books.add(this_book)
    print(this_book.title)
    return redirect('/authors')