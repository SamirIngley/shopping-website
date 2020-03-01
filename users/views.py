from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    ''' django takes care of a lot for us '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # data from our form 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('post-list-page')
    else: 
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})



# message.debug
# message.info
# message.success
# message.warning
# message.error

