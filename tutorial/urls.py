from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('snippets.urls')),
    path('', include('serializertutorial.urls')),
    path('api-auth/', include('rest_framework.urls')),
   ]
