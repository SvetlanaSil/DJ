from django.urls import path
from .views import my_view

urlpatterns = [
    # TODO добавьте здесь маршрут для вашего обработчика отображения страницы приложения landing
    path('', my_view)]
