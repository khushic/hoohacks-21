from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('grants/', include('grants.urls', namespace='grants')),
    path('research-forum/', include('forum.urls', namespace='research-forum')),
    path('student-connect/', include('connect.urls', namespace='student-connect')),
    path('events/', include('events.urls', namespace='events')),
]
