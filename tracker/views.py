from django_tables2 import SingleTableView, table_factory
from django.views import generic
from django.urls import reverse_lazy

from . import models
from . import tables
from . import forms


# Create your views here.
class APIIntegrationSummaryView(SingleTableView):
    model = models.APIIntegrationSummary
    table_class = tables.APIIntegrationSummaryTable
    template_name = "tracker/apitracksummary.html"


class CurrentStatusSummaryView(SingleTableView):
    model = models.CurrentStatus
    table_class = tables.CurrentStatusTable
    template_name = "tracker/curstatsummary.html"


class EnvironmentCredentialSummaryView(SingleTableView):
    model = models.EnvironmentCredential
    table_class = tables.EnvironmentCredentialTable
    template_name = "tracker/envcredsummary.html"


class ClientSummaryView(SingleTableView):
    model = models.Client
    table_class = tables.ClientTable
    template_name = "tracker/clientsummary.html"


class APIIntegrationCreateView(generic.CreateView):
    model = models.APIIntegrationSummary
    # form_class = forms.APIIntegrationForm
    template_name = "tracker/apitrackdetail.html"
    fields = ("client", "last_active_discussion_date", "stage",
              "important_notes", "answers_to_probing_questions",
              "interface_shared", "environment_credentials",
              "client_webhook_link", "client_webhook_sample",
              "remarks")
    success_url = reverse_lazy('tracker:apitracksummary')

    def get_context_data(self, **kwargs):
        context = super(generic.CreateView, self).get_context_data(**kwargs)

        context['table2'] = tables.CurrentStatusTable(
                    models.CurrentStatus.objects.filter(client=None))
        return context


class APIIntegrationUpdateView(generic.UpdateView):
    model = models.APIIntegrationSummary
    # form_class = forms.APIIntegrationForm
    template_name = "tracker/apitrackdetail.html"
    fields = ("client", "last_active_discussion_date", "stage",
              "important_notes", "answers_to_probing_questions",
              "interface_shared", "environment_credentials",
              "client_webhook_link", "client_webhook_sample",
              "remarks")
    success_url = reverse_lazy('tracker:apitracksummary')

    def get_context_data(self, **kwargs):
        context = super(generic.UpdateView, self).get_context_data(**kwargs)
        client = self.get_object().client
        context['apii_id'] = self.get_object().id
        context['client_id'] = client
        print(context)
        context['table2'] = tables.CurrentStatusTable(
                    models.CurrentStatus.objects.filter(client=client))
        return context


class APIIntegrationDeleteView(generic.DeleteView):
    model = models.APIIntegrationSummary
    success_url = reverse_lazy('tracker:apitracksummary')


class CurrentStatusCreateView(generic.CreateView):
    model = models.CurrentStatus
    template_name = "tracker/curstatdetail.html"
    fields = ("client", "current_status", "current_status_details")

    def get_success_url(self):
        apii_id = self.get_object().apii_id
        return reverse_lazy('tracker:apitracksummary_edit', kwargs={'pk':apii_id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        client_id = self.get_object().client_id
        self.object.client = client_id
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)
