from django.urls import path
from . import views
urlpatterns=[
    path('registration/',views.ShowFormData),
    path('hm/',views.home),
]
