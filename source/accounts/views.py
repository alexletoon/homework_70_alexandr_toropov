from django.views.generic import TemplateView, CreateView
from accounts.forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


class LoginView(TemplateView):
    template_name: str = 'login.html'
    form = LoginForm


    def get(self, request, *args, **kwargs):
        next = request.GET.get('next')
        form_data = {} if not next else {'next': next}
        form = self.form(form_data)
        context = {'form': form}
        return self.render_to_response(context)

    
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        next = form.cleaned_data.get('next', None)
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        if next:
            return  redirect(next)
        return redirect('index_view') 


def logout_view(request):
    logout(request)
    return redirect('index_view')


class RegisterView(CreateView):
    template_name: str = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index_view')
        context = {}
        context['form'] = form 
        return self.render_to_response(context)