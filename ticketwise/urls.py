"""
URL configuration for ticketwise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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


from api.views import AdminCreateView,StaffCreateView,TicketCommentView
from rest_framework.authtoken.views import ObtainAuthToken


from api.views import TicketListCreateView,TicketUpdateDeleteView,TicketRetrieveView

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/admin/register/",AdminCreateView.as_view()),

    path("api/token/",ObtainAuthToken.as_view()),

    path("api/ticket/",TicketListCreateView.as_view()),

    path("api/ticket/<int:pk>/",TicketUpdateDeleteView.as_view()),

    path("api/ticket/<int:pk>/detail/",TicketRetrieveView.as_view()),

    path("api/register/",StaffCreateView.as_view()),

    path("api/ticket/<int:pk>/comment/",TicketCommentView.as_view()),

    


]
