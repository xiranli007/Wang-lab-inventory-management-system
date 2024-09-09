from django.shortcuts import render, redirect
from .forms import CustomedUserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomedUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('user-login')
    else: 
        form = CustomedUserCreationForm()
    return render(request, 'user/register.html', {'form':form}) # the dictionary pass the 'form' instance to the html, where we can access the object using {{ form }}
