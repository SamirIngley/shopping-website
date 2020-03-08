from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    ''' django takes care of a lot for us '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # data from our form 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} account has been created! Log In')
            return redirect('login')
    else: 
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})

@login_required #login required decorator
def profile(request):
    return render(request, 'users/profile.html')


# message.debug
# message.info
# message.success
# message.warning
# message.error

