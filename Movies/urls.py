from django.contrib import admin
from django.urls import path, include

# MEDIA 파일을 설정하기 위해 IMPORT 2가지
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)