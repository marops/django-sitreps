from django.urls import path

from . import views

app_name='sitreps'

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.SitrepsListView.as_view(), name='sitreps-list'),
    path('<int:pk>/', views.SitrepsDetailView.as_view(), name='sitreps-detail'),
    path('new/',views.SitrepsCreateView.as_view(), name='sitreps-create'),
    path('<int:pk>/update/', views.SitrepsUpdateView.as_view(), name='update'),
]