
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('play.urls')), # Play
    path('admin/', admin.site.urls),
]
