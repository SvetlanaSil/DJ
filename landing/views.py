from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from .forms import MyForm


# Create your views here.
def my_view(request):
    return render(request, 'landing/index.html')


class MyTemplateView(TemplateView):
    template_name = "landing/index.html"

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data.get("Name")  # Получили очищенные данные
            Email = form.cleaned_data.get('Email')
            Subject = form.cleaned_data.get('Subject')
            Message = form.cleaned_data.get('Message')
            data = form.cleaned_data
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')
            data['ip'] = ip
            data['user_agent'] = user_agent

            return JsonResponse(data, json_dumps_params={'indent': 4, 'ensure_ascii': False})
        context = self.get_context_data(**kwargs)  # Получаем контекст, если он есть
        context["form"] = form  # Записываем в контекст форму
        return self.render_to_response(context)  # Возвращаем вызов метода render_to_response
