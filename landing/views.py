from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from landing.forms import TemplateForm



class TemplateView(View):
    def get(self, request):
        return render(request, 'landing/index.html')

    def post(self, request):
        received_data = request.POST
        form = TemplateForm(received_data)

      x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        user_agent = request.META.get('HTTP_USER_AGENT')
        return JsonResponse(data,json_dumps_params={'ensure_ascii':False,'indent':4})
    return render(request, 'landing/index.html', context={"form": form})
