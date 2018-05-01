from django.conf.urls import include, url
from django.urls import path, include

from cliente.urls import routerCliente
from mascota.urls import routerMascota
from django.contrib import admin
admin.autodiscover()


# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    path('usuarios/', include(routerCliente.urls)),
    path('mascotas/', include(routerMascota.urls)),
    path('admin/', admin.site.urls),
]
