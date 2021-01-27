from django.urls import path
from . import views

app_name = "tracker"
urlpatterns = [
    path("apitrack", views.APIIntegrationSummaryView.as_view(),
        name="apitracksummary"),
    path("curstats", views.CurrentStatusSummaryView.as_view(),
        name="curstatsummary"),
    path("envcreds", views.EnvironmentCredentialSummaryView.as_view(),
        name="envcredsummary"),
    path("clients", views.ClientSummaryView.as_view(),
            name="clientsummary"),
    path("apitracksummary/add/", views.APIIntegrationCreateView.as_view(),
            name="apitracksummary_add"),
    path("apitracksummary/edit/<pk>", views.APIIntegrationUpdateView.as_view(),
            name="apitracksummary_edit"),
    path("apitracksummary/delete/<pk>", views.APIIntegrationDeleteView.as_view(),
            name="apitracksummary_del"),
    path("curstatsummary/add", views.CurrentStatusCreateView.as_view(),
            name='curstatsummary_add'),
]
