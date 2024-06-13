from django.urls import path, include
from . import views

urlpatterns = [
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.authtoken')),
    path("", views.get_shapes, name="get_shapes"),
    path("<int:id>/", views.get_shape_id, name="get_shape_id"),
    path("create/", views.create_shape, name="create_shape"),
    path("edit/<int:id>/", views.edit_shape, name="edit_shape"),
    path("delete/<int:id>/", views.delete_shape, name="delete_shape")
    
]