from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from post import urls as p_urls
from main_page import urls as mp_urls
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from main_page import views as main_p_views
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include((p_urls, 'post'))),
    path('', include((mp_urls, 'main_page'))),
    path('login/', main_p_views.MyselfLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', main_p_views.RegisterFormView.as_view(), name='register'),
    url(r'^verify/(?P<uuid>[a-z0-9\-]+)/', main_p_views.verify, name='verify')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]\
    + urlpatterns\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
