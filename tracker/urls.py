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
        path("apitrack/add/", views.APIIntegrationCreateView.as_view(),
                name="apitrack_add"),
        path("apitrack/edit/<pk>", views.APIIntegrationUpdateView.as_view(),
                name="apitrack_edit"),
        path("apitrack/delete/<pk>", views.APIIntegrationDeleteView.as_view(),
                name="apitrack_del"),
        path("curstat/add", views.CurrentStatusCreateView.as_view(),
                name='curstat_add'),
        path("curstat/edit/<pk>", views.CurrentStatusUpdateView.as_view(),
                name="curstat_edit"),
        path("curstat/delete/<pk>", views.CurrentStatusDeleteView.as_view(),
                name="curstat_del"),
        path("envcred/add", views.EnvironmentCredentialCreateView.as_view(),
                name='envcred_add'),
        path("envcred/edit/<pk>", views.EnvironmentCredentialUpdateView.as_view(),
                name="envcred_edit"),
        path("envcred/delete/<pk>", views.EnvironmentCredentialDeleteView.as_view(),
                name="envcred_del"),
]
