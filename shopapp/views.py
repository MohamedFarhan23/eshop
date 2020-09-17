from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,ProfileForm
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .models import Product,Addcart,Buy
from django.contrib import messages
from django.contrib.auth.models import User
from .filters import Filter
#from django.contrib.auth.models import AnonymousUser 

#Home page displaying the home page and Categories
def home(request):
    current_user = request.user
    return render(request,'shopapp/home.html',{'current_user':current_user,})

#Register page creating a register form
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'shopapp/register.html',{'form':form})

# Login PAge
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
    return render(request,'shopapp/login.html',{'form':form})

# Logout method
def logout(request):
    auth.logout(request)
    return render(request,'shopapp/logout.html')

# creating profile for each user
def profile(request):
    # getting the current user
    current_user = request.user
    form = ProfileForm(instance=request.user.profile)#OneToONeField
    if request.method =='POST':
        # request file is important for image loading
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
           
    context = {'form':form,'current_user':current_user}
    return render(request,'shopapp/profile.html',context)

# creating a page for smartphones
def smartphones(request):
    # selecting a product to get its category(smartphone)
    sel_product = Product.objects.get(title='wiko')
    # filtering the category by sel_product
    product = Product.objects.filter(category=sel_product.category).all()
    return render(request,'shopapp/viewproduct.html',{'product':product})
    
# creating a page for smartphones
def laptops(request):
    # selecting a product to get its category(smartphone)
    sel_product = Product.objects.get(title='macbook')
    # filtering the category by sel_product
    product = Product.objects.filter(category=sel_product.category).all()
    return render(request,'shopapp/viewproduct.html',{'product':product})

# craeting a page for tablets
def tablets(request):
    sel_product = Product.objects.get(title='Titan')
     # filtering the category by sel_product
    product = Product.objects.filter(category=sel_product.category).all()
    return render(request,'shopapp/viewproduct.html',{'product':product})

# craeting a page for Mouse and Keyboard
def mouseandkeyboard(request):
    sel_product = Product.objects.get(title='mouse')
     # filtering the category by sel_product
    product = Product.objects.filter(category=sel_product.category).all()
    return render(request,'shopapp/viewproduct.html',{'product':product})

# craeting a page for Headphone
def headphone(request):
    sel_product = Product.objects.get(title='headphone')
     # filtering the category by sel_product
    product = Product.objects.filter(category=sel_product.category).all()
    return render(request,'shopapp/viewproduct.html',{'product':product})

# craeting a page for hometheater
def hometheater(request):
    sel_product = Product.objects.get(title='hometheater')
     # filtering the category by sel_product
    product = Product.objects.filter(category=sel_product.category).all()
    return render(request,'shopapp/viewproduct.html',{'product':product})


def addcart(request,pk):
    if request.user.is_authenticated:
        current_user = request.user
        # selecting product from Product(Model)
        sel_product = Product.objects.get(id=pk)
        # saving into Addcart model
        image = sel_product.pro_image
        title = sel_product.title
        description = sel_product.description
        price = sel_product.price
        # adding into database 
        added = current_user.addcart_set.create(cart_image=image,
                title=title,description=description,price=price)
        added.save()
        messages.success(request, 'Added successfully!')
        # important, returning to the same page
        return redirect(request.META['HTTP_REFERER'])
    else:
        messages.success(request,'you must have an account to purchase')
        return redirect('register')

def buy(request,pk):
    sel_product = Addcart.objects.get(id=pk)
    image = sel_product.cart_image
    title = sel_product.title
    description = sel_product.description
    price = sel_product.price
    order = request.user.buy_set.create(order_image=image,
            title=title,description=description,price=price)
    order.save()
    sel_product.delete()
    return redirect(request.META['HTTP_REFERER'])


# page for products in the cart
def viewcart(request):
    if request.user.is_authenticated:
        cart_product = request.user.addcart_set.all()# items in the cart
        order_product = request.user.buy_set.all() # item ordered
        return render(request,'shopapp/viewcart.html',{'cart_product':cart_product,'order_product':order_product})
    else:
        messages.success(request,'You Must a have an account to purchase')
        return redirect('register')

# removing the products from the cart
def removecart(request,pk):
    # selecting product from Product(Model)
    sel_product = Addcart.objects.get(id=pk)
    sel_product.delete()
    return redirect(request.META['HTTP_REFERER'])
