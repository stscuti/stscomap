from django.contrib import admin
from django.urls import path, include, reverse
from django.conf import settings
from Login import views
from django.conf.urls.static import static


admin.autodiscover()



urlpatterns = [
    path('', views.home, name='home'),
    path('Contacto/', views.home, name='home1'),
    path('registro/', views.registro, name='registro'),
    path('descargas/', views.descargas, name='descargas'),
    path('secret/', views.secret_page, name='secret'),
    path('Contacto/logout/', views.logout_view, name="home"),
    
    #path('secret2/', views.SecretPage.as_view(), name='secret2'),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
