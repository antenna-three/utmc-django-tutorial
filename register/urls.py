from django.urls import path
from . import views

app_name = 'register'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.ListView.as_view(), name='list'),
    path('submit/', views.submit, name='submit'),
    path('details/<int:pk>', views.DetailView.as_view(), name='details'),
    path('results/<int:pk>', views.ResultView.as_view(), name='results'),
]
