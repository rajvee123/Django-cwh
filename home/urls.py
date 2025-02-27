"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from home import views

urlpatterns = [
   path('', views.index, name='index'),
   path('about/', views.about, name='about'),
   path('menu/', views.menu, name='menu'), 
   path('contact/', views.contact, name='contact'),  # ✅ Fixed contact view
   path('booking/', views.booking, name='booking'),
   path('service/', views.service, name='service'),
   path('team/', views.team, name='team'),
   path('testimonial/', views.testimonial, name='testimonial'),
   path('register/', views.register, name='register'),
   path("login/", views.login_view, name="login"),
   path("dashboard/", views.dashboard, name="dashboard"),
   path("logout/", views.logout_view, name="logout"),
   path("mark-absent/<str:meal_type>/", views.mark_absent, name="mark_absent"),
   path("mark-multiple-absent/", views.mark_multiple_absent, name="mark_multiple_absent"),
   path("mark-absent/<str:meal_type>/", views.mark_absent, name="mark_absent"),
    path("undo-absent/<str:meal_type>/", views.undo_absent, name="undo_absent"),
    path("admin/absentees/", views.admin_absentee_report, name="admin_absentee_report"),
    path("admin/absentees/", views.admin_absentee_report, name="admin_absentee_report"),
    path("mark-multiple-absent/", views.mark_multiple_absent, name="mark_multiple_absent"),
    path("admin/mess-bill/", views.admin_mess_bill_report, name="admin_mess_bill_report"),
    path("logout/", views.logout_view, name="logout"),  # ✅ Ensure this is correct




]

