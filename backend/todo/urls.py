from rest_framework import routers

from . import views

"""Define routes"""
router = routers.DefaultRouter()
router.register(r'lists', views.TaskListsViewSet)
router.register(r'lists/(?P<list_pk>\d+)/tasks', views.TaskViewSet)

urlpatterns = router.urls
