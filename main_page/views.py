from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from main_page import forms
from django.contrib.auth.forms import UserCreationForm

class HomePage(TemplateView):
    template_name = 'main_page/base.html'


class RegisterFormView(FormView):
    form_class = forms.SignUpForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
