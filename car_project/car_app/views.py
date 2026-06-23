from django.shortcuts import render, redirect
from .models import Car, Booking,User, Expense
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Sum
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    return render(request,'index.html')

def car_list(request):

    car_view = Car.objects.all()

    return render(request,'car_list.html',{'car':car_view})


def car_details(request, id):

    car = Car.objects.get(id=id)

    return render(request,'car_details.html',{'car':car})


def car_booking(request, id):

    car = Car.objects.get(id=id)

    Booking.objects.create(
        user = request.user,
        car  = car,
    )

    messages.success(request, "Car booked successfully!")


    return redirect('car_list')


def get_register(request):

    already = ""
    success = ""

    if request.method == 'POST':

        username_reg = request.POST.get('username')
        email = request.POST.get('email')
        password_reg = request.POST.get('password')

        if User.objects.filter(email=email).exists():

            already = "Email Already Exists...."

        else:

            user = User.objects.create_user(

                username=username_reg,
                email=email,
                password=password_reg,
            )

            success = "Registration Successfully.."


    return render(request, 'register.html', {
        'already': already,
        'success': success,
    })



def get_login(request):

    login_succses = ""
    login_fail = ""

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)


        if user is not None:
            login(request,user)

            messages.success(request, f"Login Successfully {username}")

            return redirect("student_home")


        else:

            login_fail = "Username & Password Invalid"    



    return render(request,'login.html',{
        "login_succses":login_succses,
        "login_fail":login_fail,
    })


def student_home(request):

    expenses = Expense.objects.filter(user=request.user)

    total = expenses.aggregate(Sum('amount'))

    return render(request,'student_Home.html',{

        "username":request.user.username,

        "expenses":expenses,

        "total":total['amount__sum']
    })

@login_required
def add_expense(request):

    if request.method == "POST":

        title = request.POST.get('title')

        amount = request.POST.get('amount')

        category = request.POST.get('category')


        Expense.objects.create(

            user=request.user,

            title=title,

            amount=amount,

            category=category

        )


        return redirect('student_home')


    return render(request,'add_expense.html')


def delete_expense(request,id):

    expense = Expense.objects.get(
        id=id,
        user=request.user
    )

    expense.delete()


    return redirect('student_home')


def edit_expense(request,id):

    expense = Expense.objects.get(
        id=id,
        user=request.user
    )


    if request.method=="POST":


        expense.title = request.POST.get('title')

        expense.amount = request.POST.get('amount')

        expense.category = request.POST.get('category')


        expense.save()


        return redirect('student_home')


    return render(request,'edit.html',{
        'expense':expense
    })




  


