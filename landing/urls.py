from django.urls import path
from .views import TemplateView

urlpatterns = [
    # TODO добавьте здесь маршрут для вашего обработчика отображения страницы приложения landing
    path('', TemplateView.as_view(), name='template')
]