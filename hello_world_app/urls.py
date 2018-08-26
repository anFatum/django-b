from django.urls import path
from hello_world_app.views import index

app_name = 'hello_world_app'

urlpatterns = [
    path('', index, name='index'),
]
