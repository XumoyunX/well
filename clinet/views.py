from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from main.models import Category,Product, Kontak
from .forms import CategoryForm,ProductForm, KontakForm

def login_required_decorator(f):
    return login_required(f, login_url="main:login")

@login_required_decorator
def dashboard(request):
    return render(request, 'dashboard/index.html')

def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:dashboard')
    return render(request, 'dashboard/login.html')

@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('main:login')


@login_required_decorator
def category_list(request):
    categories = Category.objects.all()
    ctx = {
        'categories':categories,
        "c_active": 'active'
    }
    return render(request,'dashboard/categories/list.html',ctx)

@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/categories/form.html', ctx)

@login_required_decorator
def category_edit(request, pk):
    model = Category.objects.get(id=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:category_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/categories/form.html', ctx)

@login_required_decorator
def category_delete(request, pk):
    model = Category.objects.get(id=pk)
    model.delete()
    return redirect('main:category_list')


@login_required_decorator
def product_list(request):
    products = Product.objects.all()
    ctx = {
        'products':products,
        "p_active": 'active'
    }
    return render(request,'dashboard/products/list.html',ctx)




@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:product_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/products/form.html', ctx)

@login_required_decorator
def product_edit(request, pk):
    model = Product.objects.get(id=pk)
    form = ProductForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:product_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/products/form.html', ctx)

@login_required_decorator
def product_delete(request, pk):
    model = Product.objects.get(id=pk)
    model.delete()
    return redirect('main:product_list')




@login_required_decorator
def kontak_list(request):
    kontak = Kontak.objects.all()
    ctx = {
        'kontak':kontak,
        "k_active": 'active'
    }
    return render(request,'dashboard/kontak/list.html',ctx)

@login_required_decorator
def kontak_create(request):
    model = Kontak()
    form = KontakForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:kontak_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/kontak/form.html', ctx)

@login_required_decorator
def kontak_edit(request, pk):
    model = Kontak.objects.get(id=pk)
    form = KontakForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:kontak_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/kontak/form.html', ctx)

@login_required_decorator
def kontak_delete(request, pk):
    model = Kontak.objects.get(id=pk)
    model.delete()
    return redirect('main:kontak_list')

