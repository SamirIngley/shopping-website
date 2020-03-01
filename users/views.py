from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def register(request):
    ''' django takes care of a lot for us '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # data from our form 
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('post-list-page')
    else: 
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form':form})



# message.debug
# message.info
# message.success
# message.warning
# message.error

