from django.contrib import admin
from django.urls import path,include
from user.views import profile_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include('allauth.urls')),
    path('',include('chatapp.urls')),
    path('profile/',include('user.urls')),
    path('@<username>/', profile_view, name= "profile")
]

#only used in devlopment
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)