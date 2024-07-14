from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView

from .models import get_random_text
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from .forms import TemplateForm, CustomUserCreationForm, MyAuthenticationForm


class MyTemplView(TemplateView):
    template_name = 'app/template_form.html'

    def post(self, request, *args, **kwargs):
        received_data = request.POST

        form = TemplateForm(received_data)
        if form.is_valid():
            my_text = form.cleaned_data.get(
                "my_text")
            my_select = form.cleaned_data.get("my_select")
            my_textarea = form.cleaned_data.get("my_textarea")

            return JsonResponse(form.cleaned_data)
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return self.render_to_response(context)


class TemplView(View):
    def get(self, request):
        return render(request, 'app/template_form.html')

    def post(self, request):
        received_data = request.POST

        form = TemplateForm(received_data)
        if form.is_valid():
            my_text = form.cleaned_data.get("my_text")
            my_email = form.cleaned_data.get("my_email")
            my_password = form.cleaned_data.get("my_password")
            my_date = form.cleaned_data.get("my_date")
            my_age = form.cleaned_data.get("my_age")
            my_select = form.cleaned_data.get("my_select")
            my_textarea = form.cleaned_data.get("my_textarea")
            my_checkbox = form.cleaned_data.get("my_checkbox")
            return JsonResponse(form.cleaned_data)
        return render(request, 'app/template_form.html', context={"form": form})

    # TODO Проведите здесь получение и обработку данных если это необходимо
    # TODO Верните HttpRequest или JsonResponse с данными


class MyFormView(FormView):
    template_name = 'app/template_form.html'
    form_class = TemplateForm
    success_url = '/'

    def form_valid(self, form):
        return JsonResponse(form.cleaned_data)


class MyLoginView(LoginView):
    template_name = 'app/login.html'
    redirect_authenticated_user = True  # Данный флаг не позволит авторизированному
    # пользователю зайти на страницу с авторизацией и сразу его перенаправит на
    # ссылку редиректа. По умолчанию redirect_authenticated_user = False


def template_view(request):
    if request.method == "GET":
        return render(request, 'app/template_form.html')

    if request.method == "POST":
        received_data = request.POST  # Приняли данные в словарь

        form = TemplateForm(received_data)
        print(form)
        if form.is_valid():
            return JsonResponse(form.cleaned_data, json_dumps_params={'indent': 4, 'ensure_ascii': False})
        return render(request, 'app/template_form.html', context={"form": form})

        # как пример получение данных по ключу `my_text`
        # my_text = received_data.get('my_text')


def login_view(request):
    if request.method == "GET":
        return render(request, 'app/login.html')

    # if request.method == "POST":
    #     data = request.POST
    #     user = authenticate(username=data["username"], password=data["password"])
    #     if user:
    #         login(request, user)
    #         return redirect("app:user_profile")
    #     return render(request, "app/login.html", context={"error": "Неверные данные"})
    if request.method == "POST":
        form = MyAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("app:user_profile")
        return render(request, "app/login.html", context={"form": form})


def logout_view(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")


def register_view(request):
    if request.method == "GET":
        return render(request, 'app/register.html')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect("app:user_profile")


def reset_view(request):
    if request.method == "GET":
        return render(request, 'app/reset.html')

    if request.method == "POST":
        return render(request, 'app/register.html')


def index_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("app:user_profile")
        return render(request, 'app/index.html')


def user_detail_view(request):
    if request.method == "GET":
        return render(request, 'app/user_details.html')


def get_text_json(request):
    if request.method == "GET":
        return JsonResponse({"text": get_random_text()},
                            json_dumps_params={"ensure_ascii": False})
