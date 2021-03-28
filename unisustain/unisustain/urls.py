from django.contrib import admin
from django.urls import path, include
from accounts import views as v
from grants import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('grants/', include('grants.urls', namespace='grants')),
    #path('grants/', v2.get_all_grants, name="viewall"),
    #path('view_grants/', v2.get_grant, name="viewone"),
]
