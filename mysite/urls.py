"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import static
from mysite.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),  # 아무것도 없는경우 홈뷰로 가도록!!1
    path('blog/', include('blog.urls')),
]


urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static 함수로 인해서 media URL 이 들어오면 document root 에서 mdeia 파일을 가져와서 보여준다!