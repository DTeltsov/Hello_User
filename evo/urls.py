from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('hellouser.urls')),
    path('', RedirectView.as_view(url='/home/', permanent=True)),
]
