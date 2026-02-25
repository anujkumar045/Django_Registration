"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing,name='landing'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('userdashboard/',userdashboard,name='userdashboard'),
    path('logout/',logout,name='logout'),
    path('admindashboard/',admindashboard,name='admindashboard'),
    path('admindashboard/add_dep/',add_dep,name='add_dep'),
    path('admindashboard/save_data/',save_data,name='save_data'),
    path('admindashboard/show_dep/',show_dep,name='show_dep'),
    path('admindashboard/add_emp/',add_emp,name='add_emp'),
    path('admindashboard/save_emp/',save_emp,name='save_emp'),
    path('admindashboard/show_emp/',show_emp,name='show_emp'),
    path('admindashboard/emp_all_query/',emp_all_query,name='emp_all_query'),
    path('admindashboard/emp_all_query/reply/<int:x>/',reply,name='reply'),
    path('empdashboard/',empdashboard,name='empdashboard'),
    path('empdashboard/query',query,name='query'),
    path('empdashboard/profile',profile,name='profile'),
    path('empdashboard/setting',setting,name='setting'),
    path('empdashboard/querydata',querydata,name='querydata'),
    path('empdashboard/all_query',all_query,name='all_query'),
    path('empdashboard/pending_query',pending_query,name='pending_query'),
    path('empdashboard/done_query',done_query,name='done_query'),
    path('edit1',edit1,name='edit1'),
    path('reset',reset,name='reset'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
