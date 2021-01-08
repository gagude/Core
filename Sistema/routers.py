from rest_framework import routers
from reports.views import ArticleViewSet

#Create Your Routers Here
router = routers.DefaultRouter()
router.register(r'reports', ArticleViewSet)