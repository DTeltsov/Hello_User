from django.forms import ModelForm
from .models import User

class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']
        labels = { 'first_name': ("Ім'я"),'last_name':('Прізвище') }