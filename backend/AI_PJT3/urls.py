from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/books/', include('books.urls')),
    path('api/service_center/', include('service_center.urls')),
    path('api/voices/', include('voices.urls')),
]
