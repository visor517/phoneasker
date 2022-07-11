from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('askerbot/', include('askerbot.urls')),
    path('admin/', admin.site.urls),
]
