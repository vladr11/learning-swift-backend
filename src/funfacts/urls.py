from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register("facts", views.FunFactViewSet, base_name='facts')

urlpatterns = [url(r"^", include(router.urls))]
