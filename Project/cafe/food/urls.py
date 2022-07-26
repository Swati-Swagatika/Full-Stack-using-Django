from django.urls import path
from . import views
urlpatterns = [
    path('menu/',views.menu, name="menu"),
    path('details/<int:id>/',views.details, name="details"),
]
