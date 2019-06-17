from django.urls import path
from . import views

app_name = 'mutation'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:auto_no>/', views.chrono, name='chrono'),
    path('syndro/<int:auto_syn_code>/', views.syndro, name='syndro'),
    path('xysyndro/<int:allo_syn_code>/', views.xysyndro, name='xysyndro'),
]
