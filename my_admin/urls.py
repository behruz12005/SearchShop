from django.urls import path
# Create your views here.
from my_admin import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.SignPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('api/', views.MyApiView.as_view(), name='api'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
