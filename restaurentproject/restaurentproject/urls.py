from django.contrib import admin
from django.urls import path, include
from menu import views as menu_views
from authentication import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , menu_views.index , name='index'), 
    path('register/', auth_views.register_view, name='register'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),
    path('employment/', include('employment.urls', namespace='employment')) 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
