from django.shortcuts import get_object_or_404, render,redirect
from store.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required  
from .models import Cart, CartItem, Category, Order, OrderItem, ShippingAddress


# Create your views here.

def dashboard(request):
    popularProduct = Product.objects.all()[:6]

    ctx = {'products': popularProduct,
           'cart_items_count': get_cart_count(request)}
    return render(request, 'dashboard.html',ctx)

@login_required
def product(request):
    search = request.GET.get('search')
    products = Product.objects.all()
    filtered_products = []
    category_id = request.GET.get('category')

    
    if category_id:
        products = products.filter(category_id=category_id)
    
    selected_category = None
    if category_id:
        selected_category = Category.objects.filter(id=category_id).first()

    
    for product in products:
        if search:
            if search.lower() in product.name.lower():
                filtered_products.append(product)
        else:
            filtered_products.append(product)
    ctx = {
        'categories': Category.objects.all(),
        'cart_items_count': get_cart_count(request),
        'products' : filtered_products,
        'category': selected_category
        }

    return render(request,'product.html',ctx)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email =request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists')
            return redirect('register')
            
        User.objects.create_user(username=username,email=email,password=password)
        return redirect('loginn')

            
    return render(request,'register.html')
    

def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('loginn')
    return render(request,'login.html')

@login_required
def logoutt(request):
    logout(request)
    return redirect('loginn')

# def category_product(request, id=None):
#     categories = Category.objects.all()
#     if id:
#         products = Product.objects.filter(category_id=id)
#         category = Category.objects.get(pk=id)
#     else:
#         products = Product.objects.all()
#         category= None
        
#     return render(request, "product.html", {
#         "products": products,
#         "category": category,
#         'categories': categories,
#         })

def product_detail(request,id):
    product = Product.objects.get(id=id)
    next_url = request.GET.get('next', 'view_cart')

    return render(request,'product_detail.html',{'product':product,'cart_items_count': get_cart_count(request),"next_url":next_url
})


@login_required
def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('loginn')
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user) 

    items = CartItem.objects.filter(cart=cart)
    total = sum(item.product.price * item.quantity for item in items)
    ctx = {
        'cart': cart,
        'items': items,
        'total': total,
        'cart_items_count': get_cart_count(request)
    }
    return render(request, 'cart.html', ctx)

@login_required
def add_to_cart(request,id):
    if not request.user.is_authenticated:
        return redirect('loginn')
    try:
        cart = Cart.objects.get(user = request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user = request.user)
        
    product = Product.objects.get(id=id)
    
    try: 
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=1)
        
    next_url = request.GET.get('next', 'view_cart')
    return redirect(next_url)
    
@login_required
def get_cart_count(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        return CartItem.objects.filter(cart=cart).count()
    return 0

@login_required
def contact(request):
    if not request.user.is_authenticated:
        return redirect('loginn')
    return render(request,'contact.html',{'cart_items_count': get_cart_count(request)})

@login_required
def remove_cartItem(request,id):

    CartItem.objects.filter(id=id).delete()
    return redirect('view_cart')

@login_required
def increase_q(request,id):

    Q = CartItem.objects.get(id=id)
    Q.quantity +=1
    Q.save()
    return redirect('view_cart')
    
@login_required
def decrease_q(request,id):

    Q = CartItem.objects.get(id=id)
    Q.quantity -=1
    if Q.quantity<=0:
        Q.delete()
    else:
        Q.save()
    return redirect('view_cart')

@login_required
def checkout(request):
    if not request.user.is_authenticated:
        return redirect('loginn')
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)  # or session-based
    if request.method == "POST":
        # Create order
        order = Order.objects.create(
            user=request.user,
            total_amount=sum(item.product.price * item.quantity for item in cart_items),
            status="pending"
        )

        # Save order items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Save shipping address
        ShippingAddress.objects.create(
            order=order,
            full_name=request.POST.get("full_name"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            postal_code=request.POST.get("postal_code")
        )
        

        # Clear cart after checkout
        cart_items.delete()

        return redirect("success", order_id=order.id)

    return render(request, "checkout.html", {"cart_items": cart_items})

@login_required
def order_success(request, order_id):
    if not request.user.is_authenticated:
        return redirect('loginn')
    order = get_object_or_404(Order, id=order_id)
    return render(request, "order_success.html", {"order": order})