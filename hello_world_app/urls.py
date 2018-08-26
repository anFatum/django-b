from django.urls import path
from hello_world_app.views import index

urlpatterns = [
    path('', index),
]
