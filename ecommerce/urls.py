from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path("", include("products.urls")),
    path("accounts/", include("accounts.urls")),
    path("cart/", include("carts.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT ) #para visualizar las imagenes
