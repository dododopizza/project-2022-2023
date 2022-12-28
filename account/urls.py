from django.contrib import admin, auth
from django.urls import path, include
from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('edit_profile/', views.edit_profile, name="edit"),
    path('edit_projects/', views.edit_projects, name="editpr"),
    re_path(r'^profile/(?P<pk>[-\w]+)/$', views.profile, name="profile"),
    path('logout/', views.Logout, name="logout"),
    re_path(r'^profile/(?P<pk>[-\w]+)/project/$', views.project, name="project"),
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)