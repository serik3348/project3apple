from django.urls import path
from . import views
urlpatterns = [
    path('', views.register_request, name="register"),
    path('send2', views.send_message1, name="send2"),
    path('send1', views.send_message, name="send1")
]