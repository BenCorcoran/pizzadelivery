from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import PizzaForm, RegisterForm, DeliveryDetailsForm
from .models import DeliveryDetails, Pizza

def index(request):
    return render(request, 'index.html')

def neworder(request):

    orders = Pizza.objects.filter(user=request.user)
    
    return render(request, 'neworder.html', {'orders': orders})

def orderdetails(request):
    pizza = Pizza.objects.filter(user=request.user).last()  # Get the last pizza order
    delivery = DeliveryDetails.objects.filter(user=request.user).last()  # Get the last delivery details
    
    if pizza and delivery:
        context = {
            'pizza': pizza,
            'delivery': delivery
        }
    else:
        context = {
            'error': "No order found. Please complete your order first."
        }
    
    return render(request, 'orderdetails.html', context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("neworder")  # Redirect to orders page after registration
    else:
        form = RegisterForm()

    return render(request, "index.html", {"form": form})

def createpizza(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.user = request.user
            pizza.save()
            return redirect("details")  # Redirect to order summary
    else:
        form = PizzaForm()

    return render(request, "createpizza.html", {"form": form})

def previous_orders(request):
    orders = Pizza.objects.filter(user=request.user)
    return render(request, "neworder.html", {"orders": orders})

def details(request):
    if request.method == "POST":
        form = DeliveryDetailsForm(request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.user = request.user  # Assign the logged-in user
            delivery.save()
            return redirect('orderdetails')  # Change to the next step
    else:
        form = DeliveryDetailsForm()
    
    return render(request, 'details.html', {'form': form})
