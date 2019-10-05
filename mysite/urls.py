"""mysite URL Configuration

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
from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth_view
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('profile/<int:pk>',user_view.profileview.as_view(), name="profile"),
    path('profile/<int:pk>/update/',user_view.patientupdateview.as_view(), name="patient_update"),
    path('register/', user_view.create_user , name="register"),
    path('addpatient/', user_view.patientregister_view , name="addpatient"),
    path('login/', auth_view.LoginView.as_view(template_name="user/login.html") , name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name="user/logout.html") , name="logout"),
]
if settings.DEBUG:
    urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)