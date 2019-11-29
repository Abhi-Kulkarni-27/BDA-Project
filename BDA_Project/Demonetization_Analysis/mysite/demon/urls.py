from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exec', views.exec, name='exec'),
    path('visualize', views.viz, name='visualize'),
    path('about', views.about, name='about'),
    path('result', views.result, name='result'),
    path('positive', views.positive, name='positive'),
    path('negetive', views.negetive, name='negetive'),
    path('neutral', views.neutral, name='neutral'),
]
