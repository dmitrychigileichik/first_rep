from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from main_page import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.shortcuts import render, redirect
from main_page.models import User
from django.contrib.auth.views import LoginView



class MyselfLoginView(LoginView):
    template_name = "login.html"
    form_class =  forms.MyAuthenticationForm

class HomePage(TemplateView):
    template_name = 'main_page/base.html'


class RegisterFormView(FormView):
    form_class = forms.SignUpForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


def home(request):
    return render(request, 'main_page/base.html')
 
 
def verify(request, uuid):
    try:
        user = User.objects.get(verification_uuid=uuid, is_verified=False)
    except User.DoesNotExist:
        raise Http404("User does not exist or is already verified")
 
    user.is_verified = True
    user.save()
 
    return redirect('main_page:home')
