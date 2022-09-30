from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Book,student
from .forms import BookForm
from django.contrib.auth.models import Group
from django.db.models import Q
from . import forms,models
from django.contrib.auth.decorators import login_required,user_passes_test

def index(request):
    return render(request, 'index.html')

def adminclick_view(request):
    if request.user.is_authenticated:
         return HttpResponseRedirect('afterlogin')
    return render(request,'adminclick.html')


def adminsignup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()


            my_admin_group = Group.objects.get_or_create(name='')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('adminlogin')
    return render(request,'adminsignup.html',{'form':form})



def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def afterlogin_view(request):
        return render(request, 'adminafterlogin.html')


def viewstudent_view(request):
    students=models.student.objects.all()
    return render(request,'viewstudent.html',{'students':students})


def Book_list(request):

    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    Books = Book.objects.filter(
        Q(Bookname__icontains=search_query) | 
        Q(Author__icontains=search_query) 
    )

    context = {
        'Books': Books,
        'search_query': search_query,
    }
    
    return render(request, 'list.html', context)
    

def create(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Book-list')

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

def edit(request, pk):
    Books = Book.objects.get(id=pk)
    form = BookForm(instance=Books)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=Books)
        if form.is_valid():
            form.save()
            return redirect('Book-list')

    context = {
        'Book': Books,
        'form': form,
    }
    return render(request, 'edit.html', context)


def delete(request, pk):
    Books = Book.objects.get(id=pk)

    if request.method == 'POST':
        Books.delete()
        return redirect('Book-list')

    context = {
        'Book': Books,
    }
    return render(request, 'delete.html', context)