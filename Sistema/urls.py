from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from tickets import views
from users import views as us

router = routers.DefaultRouter()
router.register(r'users', us.UserViewSet)
router.register(r'groups', us.GroupViewSet)
router.register(r'ticketsAPI', views.TicektsViewSet)
router.register(r'ligacoesAPI', views.LigacoesViewSet)

urlpatterns = [
    path('', include("users.urls")),
    path('admin/', admin.site.urls),
    path('tickets/', include("tickets.urls")),
    path('tasks/', include("tasks.urls")),
    path('', include(('tasks.urls', 'tasks'), namespace='tasks')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]





# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
