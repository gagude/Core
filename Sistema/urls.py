from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from tickets import views
from users import views as us
from vueshow import views as myapp_views
from .routers import router as otherRouter
from django.views.generic import TemplateView
from reports.views import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'users', us.UserViewSet)
router.register(r'groups', us.GroupViewSet)
router.register(r'ticketsAPI', views.TicektsViewSet)
router.register(r'ligacoesAPI', views.LigacoesViewSet)
router.register(r'reports', ArticleViewSet)

urlpatterns = [
    path('', include("users.urls")),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('tickets/', include("tickets.urls")),
    path('tasks/', include("tasks.urls")),
    path('report/', include("reports.urls")),
    path('', include(('tasks.urls', 'tasks'), namespace='tasks')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('myteste/', myapp_views.frontend),
    path('myteste/article/', myapp_views.frontend),
    path('myteste/author/', myapp_views.frontend),
    path('myteste/article/<slug:slug>/', myapp_views.frontend),
    path('myteste/author/<slug:slug>/', myapp_views.frontend),
]





# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
