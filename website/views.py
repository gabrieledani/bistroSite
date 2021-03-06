from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, UserProfileForm, MakeReservation
from .models import Reservation, UserProfile
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def index(request):
	return render(request,'index.html',{})

def home(request):
    if request.user.is_authenticated:
        reservation_list = Reservation.objects.filter(user_id = request.user)
        total =0
        total_f = '0,00'
        number = 0
        can_change = True
        for reservation in reservation_list:
            total = total + reservation.price
            total_f = '{:.2f}'.format(total)
            number = number + 1
            if number >=8:
                can_change = False
        context = {'reservation_list': reservation_list,'total':total_f,'number':number,'can_change':can_change}
    else:
        context = {}
    return render(request, 'home.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #messages.success(request, ('Logged In'))
            return redirect('home')
            # Redirect to a success page.
        else:
            messages.success(request, ('Erro de Autenticação. Revise os dados ou efetue seu cadastro.'))
            return redirect('login')
            # Return an 'invalid login' error message.
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    #messages.success(request,'Logout')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            #messages.success(request, ('Registered....'))

            return redirect('reservation')
    else:
        form = SignUpForm()
        profile_form = UserProfileForm()

    context = {'form':form,'profile_form': profile_form}
    return render(request, 'register.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            #messages.success(request, ('You Have Edited Your Profile...'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    context = {'form': form,'profile_form': profile_form}
    return render(request, 'edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            #messages.success(request, ('You Have Edited Your Password...'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'change_password.html', context)

def reservation(request):
    submitted = False
    if request.method == 'POST':
        form = MakeReservation(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            if reservation.kids_menu:
                reservation.price = 55
            else:
                reservation.price = 110
            form.save()

            return HttpResponseRedirect('/reservation?submitted=True')
    else:
        form = MakeReservation()
        if 'submitted' in request.GET:
            submitted=True
        context = {'form': form,'submitted':submitted}

    return render(request,'reservation.html',context)

def final(request):
    user_list = UserProfile.objects.all().order_by('user_id')
    reservation_list = Reservation.objects.all().order_by('user_id')
    context = {'user_list':user_list,'reservation_list':reservation_list}
    return render(request,'final.html',context)
