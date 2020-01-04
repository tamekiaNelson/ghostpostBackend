"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from ghostpost import views
from ghostpost.models import GhostPoster

admin.site.register(GhostPoster)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='/'),
    path('addpost/', views.ghostpostaddview, name='addpost'),
    path('upvote/<int:id>/', views.up_votes, name='upvote'),
    path('downvote/<int:id>/', views.down_votes, name='downvote'),
    path('boasts/', views.sort_is_a_boast, name='boast'),
    path('roasts/', views.sort_is_a_roast, name='roast'),
    path('all/', views.sort_all_posts, name='all')
]
