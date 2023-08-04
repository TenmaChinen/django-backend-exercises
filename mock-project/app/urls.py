from django.views.generic import RedirectView
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='bookstores/list/')),
    path('bookstores/', include('bookstores.urls')),
]
