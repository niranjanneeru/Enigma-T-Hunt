from django.urls import path

from .views import (
    profile_view
)

app_name = "user_profile"
urlpatterns = [
    path("profile/", view=profile_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
