from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/gp', LeadViewSet, 'gp')

urlpatterns = router.urls