from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Hotel, PizzaHut, Dominos, Toppings, OMR, NMR, Kapilavastu, Malabar, UserOrder, SavedCarts
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout, authenticate, login
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        #we are passing in the data from the category model
        return render(request, "orders/home.html", {"categories":Hotel.objects.all})
    else:
        return redirect("orders:login")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('/')

    form = AuthenticationForm()
    return render(request = request,
                    template_name = "orders/login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    return redirect("orders:login")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("orders:login")

        return render(request = request,
                          template_name = "orders/register.html",
                          context={"form":form})

    return render(request = request,
                  template_name = "orders/register.html",
                  context={"form":UserCreationForm})

def pizzahut(request):
    if request.user.is_authenticated and request.method =='GET':
        dishes = PizzaHut.objects.all()
        paginated_sici = Paginator(dishes, 3)
        page_number2 = request.GET.get('page2') #Get the requested page number from the URL
        page2 = paginated_sici.get_page(page_number2)

        context = { "sicillian_pizza": page2, "toppings":Toppings.objects.all}
        return render(request, "orders/pizzahut.html", context =context)
    elif request.user.is_authenticated and request.method == 'POST':
        rating = request.POST.get('rtg')
        pid = request.POST.get('pid')
        print('##############')
        print(rating, pid, request.POST)
        dish = PizzaHut.objects.get(id = int(pid))
        dish.rating =rating
        dish.save()
        return redirect('orders:pizzahut')
    else:
        return redirect("orders:login")


def dominos(request):
    if request.user.is_authenticated and request.method =='GET':

        dishes = Dominos.objects.all()
        paginated_reg = Paginator(dishes, 3)
        page_number1 = request.GET.get('page') #Get the requested page number from the URL
        page1 = paginated_reg.get_page(page_number1)
        context = {"regular_pizza": page1, "toppings":Toppings.objects.all}
        return render(request, "orders/dominos.html", context =context)
    elif request.user.is_authenticated and request.method == 'POST':
        rating = request.POST.get('rtg')
        pid = request.POST.get('pid')
        print('##############')
        print(rating, pid, request.POST)
        dish = Dominos.objects.get(id = int(pid))
        dish.rating =rating
        dish.save()
        return redirect('orders:dominos')
        
    else:
        return redirect("orders:login")

def omr(request):
    if request.user.is_authenticated and request.method =='GET':
        dishes = OMR.objects.all()
        paginated = Paginator(dishes, 3)
        page_number = request.GET.get('page1') #Get the requested page number from the URL
        page = paginated.get_page(page_number)

        return render(request, "orders/omr.html", context = {"dishes":page})
    elif request.user.is_authenticated and request.method == 'POST':
        rating = request.POST.get('rtg')
        pid = request.POST.get('pid')
        print('##############')
        print(rating, pid, request.POST)
        dish = OMR.objects.get(id = int(pid))
        dish.rating =rating
        dish.save()
        return redirect('orders:omr')
    else:
        return redirect("orders:login")


def nmr(request):
    if request.user.is_authenticated and request.method =='GET':
        dishes = NMR.objects.all()
        paginated = Paginator(dishes, 3)
        page_number = request.GET.get('page') #Get the requested page number from the URL
        page = paginated.get_page(page_number)

        return render(request, "orders/nmr.html", context = {"dishes":page})
    elif request.user.is_authenticated and request.method == 'POST':
        rating = request.POST.get('rtg')
        pid = request.POST.get('pid')
        print('##############')
        print(rating, pid, request.POST)
        dish = NMR.objects.get(id = int(pid))
        dish.rating =rating
        dish.save()
        return redirect('orders:nmr')
    else:
        return redirect("orders:login")


def kapilavastu(request):
    if request.user.is_authenticated and request.method =='GET':
        dishes = Kapilavastu.objects.all()
        paginated = Paginator(dishes, 3)
        page_number = request.GET.get('page') #Get the requested page number from the URL
        page = paginated.get_page(page_number)
        return render(request, "orders/kapilavastu.html", context = {"dishes":page})
    elif request.user.is_authenticated and request.method == 'POST':
        rating = request.POST.get('rtg')
        pid = request.POST.get('pid')
        print('##############')
        print(rating, pid, request.POST)
        dish = Kapilavastu.objects.get(id = int(pid))
        dish.rating =rating
        dish.save()
        return redirect('orders:kapilavastu')
    else:
        return redirect("orders:login")


def malabar(request):
    if request.user.is_authenticated and request.method =='GET':
        dishes = Malabar.objects.all()
        paginated = Paginator(dishes, 3)
        page_number = request.GET.get('page') #Get the requested page number from the URL
        page = paginated.get_page(page_number)
        return render(request, "orders/malabar.html", context = {"dishes":page})
    elif request.user.is_authenticated and request.method == 'POST':
        rating = request.POST.get('rtg')
        pid = request.POST.get('pid')
        print('##############')
        print(rating, pid, request.POST)
        dish = Malabar.objects.get(id = int(pid))
        dish.rating =rating
        dish.save()
        return redirect('orders:malabar')
    else:
        return redirect("orders:login")

def directions(request):
    if request.user.is_authenticated :
        return render(request, "orders/directions.html")
    else:
        return redirect("orders:login")

def hours(request):
    if request.user.is_authenticated :
        return render(request, "orders/hours.html")
    else:
        return redirect("orders:login")

def contact(request):
    if request.user.is_authenticated :
        return render(request, "orders/contact.html")
    else:
        return redirect("orders:login")

def cart(request):
    if request.user.is_authenticated :
        return render(request, "orders/cart.html")
    else:
        return redirect("orders:login")

def checkout(request):
    if request.method == 'POST':
        cart = json.loads(request.POST.get('cart'))
        price = request.POST.get('price_of_cart')
        username = request.user.username
        response_data = {}
        list_of_items = [item["item_description"] for item in cart]

        order = UserOrder(username=username, order=list_of_items, price=float(price), delivered=False) #create the row entry
        order.save() #save row entry in database

        response_data['result'] = 'Order Recieved!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def view_orders(request):
    if request.user.is_superuser:
        #make a request for all the orders in the database
        rows = UserOrder.objects.all().order_by('-time_of_order')
        #orders.append(row.order[1:-1].split(","))

        return render(request, "orders/orders.html", context = {"rows":rows})
    else:
        rows = UserOrder.objects.all().filter(username = request.user.username).order_by('-time_of_order')
        return render(request, "orders/orders.html", context = {"rows":rows})

def mark_order_as_delivered(request):
    if request.method == 'POST':
        
        id = request.POST.get('id')
        UserOrder.objects.filter(pk=id).update(delivered=True)
        return HttpResponse(
            json.dumps({"good":"boy"}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def save_cart(request):
    if request.method == 'POST':
        cart = request.POST.get('cart')
        saved_cart = SavedCarts(username=request.user.username, cart=cart) #create the row entry
        saved_cart.save() #save row entry in database
        return HttpResponse(
            json.dumps({"good":"boy"}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def retrieve_saved_cart(request):
    saved_cart = SavedCarts.objects.get(username = request.user.username)
    return HttpResponse(saved_cart.cart)

def check_superuser(request):
    print(f"User super??? {request.user.is_superuser}")
    return HttpResponse(request.user.is_superuser)
