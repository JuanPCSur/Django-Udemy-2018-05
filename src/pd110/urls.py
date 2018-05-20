"""pd110 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url 
from django.conf import settings            #Clase 22
from django.conf.urls.static import static  #Clase 22
from django.contrib import admin

from boletin import views
from .views import about
#from boletin.views inicio


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^about$', about, name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        # MEDIA_URL no existia.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
