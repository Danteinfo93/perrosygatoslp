from rest_framework import routers

from .viewsets import ProfileViewSet, TrainerViewSet, AdViewSet, AdoptionViewSet, StrayingViewSet, FindingViewSet, CrossViewSet, BreedViewSet, LocationViewSet

router = routers.SimpleRouter()
router.register('profiles', ProfileViewSet)
router.register('trainers', TrainerViewSet)
router.register('ads', AdViewSet)
router.register('adoptions', AdoptionViewSet)
router.register('strayings', StrayingViewSet)
router.register('findings', FindingViewSet)
router.register('crosses', CrossViewSet)
router.register('breeds', BreedViewSet)
router.register('locations', LocationViewSet)


urlpatterns = router.urls