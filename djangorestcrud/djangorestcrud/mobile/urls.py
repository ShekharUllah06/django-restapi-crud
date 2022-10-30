from django.urls import path
from mobile import views

urlpatterns = [
    path("", views.ListMobileAPIView.as_view(), name="list_mobile"),
    path("create/", views.CreateMobileAPIView.as_view(), name="create_mobile"),
    path("update/<int:pk>/", views.UpdateMobileAPIView.as_view(), name="update_mobile"),
    path("delete/<int:pk>/", views.DeleteMobileAPIView.as_view(), name="delete_mobile")
]
