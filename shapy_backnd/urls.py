from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", include("main.urls")), #admin
    path("user/", include("main_user.urls")), #user

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
