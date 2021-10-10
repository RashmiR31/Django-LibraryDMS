from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    shelf = Book.objects.all()
    return render(request,'library.html',{'shelf':shelf})

def upload_book(request):
    upload = BookForm()
    if request.method=='POST':
        upload = BookForm(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request,'upload_form.html',{'upload_form':upload})

def update_book(request,book_id):
    book_id=int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookForm(request.POST or None,instance = book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request,'upload_form.html',{'upload_form':book_form})

def delete_book(request,book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')