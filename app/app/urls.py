"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from web.views import HomeView, EntryFormView, CSVUploaderView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('entries/', EntryFormView.as_view(), name="entries"),
    path('csv_upload/', CSVUploaderView.as_view(), name="csv_uploader"),
    path('admin/', admin.site.urls),
]
