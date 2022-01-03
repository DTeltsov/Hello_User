from .models import User
from django.shortcuts import render
from .forms import UserModelForm
# Create your views here.
def index(request): 
    form = UserModelForm(request.POST)
    if form.is_valid(): 
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        try:
            user = User.objects.get(first_name=first_name, last_name=last_name)
            greetings = 'Вже бачились, ' + first_name + ' ' + last_name
            return render(request,'greetings.html', {'greetings':greetings})
        except User.DoesNotExist:
            greetings = 'Привіт, ' + first_name + ' ' + last_name
            user = User()
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return render(request,'greetings.html', {'greetings':greetings})
    return render(request,'index.html', {'form': form})


def get_all_users(request):
    users = User.objects.all()
    return render(request, 'all_users.html', {'users': users})

