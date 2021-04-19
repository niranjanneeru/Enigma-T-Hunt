from django.urls import path

from .views import (
    question_view
)

app_name = "game"
urlpatterns = [
    path("ques/", view=question_view, name="quiz"),
]
