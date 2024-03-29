"""sargam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from pages.views import home_view, about_view, contact_view, community_view
from members.views import login_view, loggedin_view, logout_view, register_user

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view),
    path('contact/', contact_view),
    path('community/', community_view),
    path('login/', login_view, name='log_in'),
    path('logout/', logout_view, name='logged_out'),
    path('register/', register_user, name='register_user'),
    path('<str:username>/', loggedin_view, name='loggedIn'),
    path('billing/', admin.site.urls),
]

admin.site.site_header = "Sargam: Administration Page"
admin.site.site_title = "Sargam Administration"
admin.site.index_title = "Welcome to Sargam Admin Panel"
