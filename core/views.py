from django.shortcuts import render, redirect
import random
from django.views.generic.edit import FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = 'core/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
      return reverse_lazy('fortune')


class RegisterPage(FormView):
    template_name = 'core/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('fortune')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('fortune')
        return super(RegisterPage, self).get(*args, **kwargs)


fortuneList = [
  "Today is a good day to work-hard",
  "Eat, sleep, gym, work repeat",
  "You are getting that job soon",
  "You should trust yourself more",
  "Every think is possible. Don't forget it!",
  "Learn as if you will live forever, live like you will die tomorrow.",
  "Success is getting what you want, happiness is wanting what you get.",
  "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.",
  "When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.",

]


def fortune(request):
  fortune = random.choice(fortuneList)
  context_1 = {"fortune": fortune}
  return render(request,'core/fortune.html', context_1)

