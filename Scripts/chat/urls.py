from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from chat_engine import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
   ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
