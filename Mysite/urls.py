from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #on pointe vers noyau
    path('', include('noyau.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls'))
]
