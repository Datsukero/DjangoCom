"""DjangoCom URL Configuration

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
# importacao das config nova dos settings
from django.conf import settings
# importacao da pasta static
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

# import dos perfis sendo a pasta views possuindo os html 
from profiles import views as profiles_views
from contact import views as contact_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profiles_views.home, name='home'),
    url(r'^sobre/$', profiles_views.sobre, name='sobre'),
    url(r'^contato/$', contact_views.contact, name='contato'),
]

if settings.DEBUG:
	urlpatterns == static(settings.STATIC_URL, documment_root=settings.STATIC_ROOT)
	urlpatterns == static(settings.MEDIA_URL, documment_root=settings.MEDIA_ROOT)