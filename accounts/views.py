from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return render(request, 'schamas/schemas.html')
            return HttpResponse("Authorized successfully")

    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
