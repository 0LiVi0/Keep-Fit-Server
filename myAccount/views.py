from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from myAccount.forms import RegisterForm
from restAccount.models import DriverUser


def register(request):

	if request.user.is_authenticated:
		return redirect('myAccount:logout')
	else:
		if request.method == 'POST':
			form = RegisterForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('myprofile:list')
		else:
			form = RegisterForm()

			args = {'form':form}
			return render(request, 'myAccount/register.html')