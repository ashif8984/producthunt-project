from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

from django.contrib import auth, messages
from .forms import UserRegistrationForm
# from .forms import Login

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) # form with data=request.POST
        if form.is_valid(): # checks backend validtion like- password dont match, user already present
            form.save()
            username = form.cleaned_data.get('username') # a dictionary
            messages.success(request, f'Your Account created! You can login now')
            return redirect('login')

    else:
        form = UserRegistrationForm() # Empty Form
    return render(request, 'accounts/register.html', {'form': form})
'''
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


def signup(request):
    
    if request.method == 'POST':
        # The User has info and wants account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has been taken'})
            except User.DoesNotExist:
                user =  User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):

    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None and form.is_valid():
            auth.login(request, user)
            return redirect('home')
        else:
            #return render(request, 'accounts/login.html', {'error':'Username or Passoword is incorrect'})
            return render(request, "accounts/login.html", context) 
    else:
        return render(request, 'accounts/login.html')

# DataFlair #Form #View Functions
def loginform(request):
    # form = forms.Login()
    if request.method == 'POST':

        # user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        form = Login(request.POST)
        if form.is_valid():
            pass
        
    else:
        form = Login()
    
    return render(request, 'accounts/login2.html', {'form': form})

    
        if user is not None:
            auth.login(request, user)
            # html = html + "The Form is Valid"
            return redirect('home')
        else:
            #html = 'welcome for first time'
            return render(request, 'accounts/login2.html', {'form': form})
    else: 
        return render(request, 'accounts/login2.html')

    
def logout(request):

    # TODO: need to rouet to homepage
    # and dont forgot to logout
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

'''