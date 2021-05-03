from django.urls import path
from . import views
app_name="WebApp"
urlpatterns = [
    path('item/',views.Items,name='item'),
    path('cre/',views.create,name='cre'),
    path('pro/',views.Cook,name='process'),
    path('dtail/<int:id>/',views.detail,name="dtail"),
    path('dlte/<int:id>/',views.delete,name="dlte"),

]