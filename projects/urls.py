from rest_framework import routers
from .api import ProjectViewSet 
router= routers.DefaultRouter()

router.register("api/projects", ProjectViewSet , "projects")  # Creacion de las rutas.         

urlpatterns =  router.urls


    