from django.urls import path
from django.http import HttpResponse

app_name = 'payapp'

urlpatterns = [
    path('', lambda x: HttpResponse('<h1>Hi there!</h1>'), name='hello'),
]
