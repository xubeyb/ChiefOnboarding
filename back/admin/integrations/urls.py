from django.urls import path

from . import views

app_name = "integrations"
urlpatterns = [
    path("slack", views.SlackOAuthView.as_view()),
    path("create", views.IntegrationCreateView.as_view(), name="create"),
    path("update/<int:pk>/", views.IntegrationUpdateView.as_view(), name="update"),
    path(
        "update_creds/<int:pk>/",
        views.IntegrationUpdateExtraArgsView.as_view(),
        name="update-creds",
    ),
]
