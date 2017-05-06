from django.conf.urls import url
from aah import views
from django.conf import settings
from django.conf.url.static import static

urlpatterns = [
        url(r'^$', views.index, name='home'),
        


] + static(setting.STATIC_URL,document_root=settings.STATIC_ROOT

