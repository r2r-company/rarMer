from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from rarMer.views import home

urlpatterns = [
    path('', home, name='home'),
    path('tasks/', include('tasks.urls')),
    path('companies/', include('companies.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/', include('api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('access/', include('access.urls')),
    path('profile/', include('userprofile.urls')),
    path('nomenklatyra/', include('nomenklatyra.urls')),
    path('equipment/', include('equipment.urls')),
    path('workers/', include('workers.urls')),
    path('zapravka/', include('zapravka.urls')),
    path('siteorder/', include('siteorder.urls')),

]
