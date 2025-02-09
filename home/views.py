from django.shortcuts import render,HttpResponseRedirect
from home.forms import PasswordForm
import random
import string

def passwords(request):
    password = ""
    length=12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Create your views here.
def generate_password(request):
      password = ""
      form = PasswordForm()
      if request.method == "POST":
            form = PasswordForm(request.POST)
            if form.is_valid():
                length = form.cleaned_data['length']
                length = int(length)
                characters = string.ascii_letters + string.digits 
                password = ''.join(random.choice(characters) for _ in range(length))
                # return HttpResponseRedirect('/password')
      context = {
           "password": password,
           "form":form
      }
      return render(request,"index.html",context)
