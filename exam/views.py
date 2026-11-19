from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *










def registration(request):
    if request.method == 'POST':
        data = request.POST
        if data:
            if data:
                CustomUser.objects.create_user(
                    username = data['username'],
                    password = data['password'],
                    email = data.get('email', ''),
                    photo = request.FILES.get('photo'),
                    phone = data.get('phone', ''),
                    about = data.get('about', '')
                )
            else:
                return redirect('register')
        else:
            return redirect('register')
        return redirect('login')
    return render(request, 'registration.html')




def login_user(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate (
            request,
            username = data['username'],
            password = data['password']
        )
        if user is not None:
            login(request, user)
            return redirect('show_stadiums')
        return redirect('register')
    return render(request, 'login.html')



@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')


@login_required
def create_stadium(request):
    if request.method == 'POST':
        Stadium.objects.create(
            caption = request.POST['caption'],
            location = request.POST['location'],
            category_id = request.POST['category'],
            price = request.POST['price'],
            image = request.FILES['image']
        )
        return redirect('show_stadiums')


    categories = Category.objects.all()
    return render(request, 'create_stadium.html', {'categories': categories})




@login_required
def show_stadiums(request):
    stad = Stadium.objects.filter(is_free=True)
    categories = Category.objects.all()

    return render(request, 'home.html', {'stad': stad, 'categories': categories})


@login_required
def search(request):
    stad = Stadium.objects.filter(is_free=True)
    categoria = Category.objects.all()
    category = request.GET.get('category')

    if category:
        stad = stad.filter(category_id=category)

    return render(request, 'home.html', {'stad': stad, 'categories': categoria})







@login_required
def stadium_info(request, pk):
    stadium = Stadium.objects.get(pk=pk, is_free=True)
    return render(request, 'stadium_info.html', {'stadium': stadium})







@login_required
def my_stadium(request):
    book = request.user.my_booked_stadium_set.filter(status=True)
    return render(request, 'my_stadium.html', {'book': book})





@login_required
def finish_game(request, pk):
    if request.method == 'POST':
        booking = My_booked_stadium.objects.get(pk=pk, user=request.user)

        if booking.status:
            booking.status =False
            booking.save()

            booking.stadium.is_free = True
            booking.stadium.save()

    return redirect('my')


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

    
    

    
    
    
@login_required
def book_stadium(request, pk):
    stadium = Stadium.objects.get(pk=pk, is_free=True)

    if request.method == 'POST':
        My_booked_stadium.objects.create(
            user=request.user,
            stadium=stadium,
            playears_needad=request.POST['playears_needad'],
            status=True
        )

        stadium.is_free = False
        stadium.save()
        return redirect('my')

    return render(request, 'book_stadium.html', {'stadium': stadium})







@login_required
def join_game(request, pk):
    if request.method == 'POST':
        booking = My_booked_stadium.objects.get(pk=pk)
        if booking.status:
            Particplant.objects.create(
                booking=booking,
                user=request.user
            )

    return redirect('show_stadiums')


@login_required
def play_together(request):
    book = My_booked_stadium.objects.filter(status=True, playears_needad__gt = 0)

    return render(request, 'play_together.html', {'book': book})


@login_required
def delete_game(request, pk):
    if request.method == 'POST':
        req = Particplant.objects.filter(booking_id=pk, user=request.user)
        req.delete()

    return redirect('games')






