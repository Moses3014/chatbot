from os import name
from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'chats', views.ChatViewSet)
# router.register(r'getchat', )

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('',views.index,name="index"),
    path('getChat',views.getChat,name="get-chats"),
    path('setChat',views.setChat,name="set-chats"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
