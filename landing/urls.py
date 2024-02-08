from django.urls import path
from .views import my_view,MyTemplateView

app_name = 'landing'

urlpatterns = [
    # TODO добавьте здесь маршрут для вашего обработчика отображения страницы приложения landing
#    path('', my_view),
    path('', MyTemplateView.as_view(), name='template')]
