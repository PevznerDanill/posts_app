"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to pages. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function pages
    1. Add an import:  from my_app import pages
    2. Add a URL to urlpatterns:  path('', pages.home, name='home')
Class-based pages
    1. Add an import:  from other_app.pages import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app_posts.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
