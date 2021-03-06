from django_tables2 import SingleTableView
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from . import models
from . import tables


# Create your views here.
class APIIntegrationSummaryView(SingleTableView):
    model = models.APIIntegrationSummary
    table_class = tables.APIIntegrationSummaryTable
    template_name = "tracker/apitracksummary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['back_to_apii'] = self.request.path
        
        return context

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
        context = super().get_context_data(**kwargs)
        # context['back_to_apii'] = self.request.session['back_to_apii']

        self.request.session['back_to_curstat'] = self.request.path
        self.request.session['back_to_envcred'] = self.request.path
        context['table_curstatsummary'] = tables.CurrentStatusTable(
                    models.CurrentStatus.objects.filter(client=None))
        context['table_envcredsummary'] = tables.EnvironmentCredentialTable(
                    models.EnvironmentCredential.objects.filter(client=None))
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
        context = super().get_context_data(**kwargs)

        self.request.session['apii_id'] = self.get_object().id
        self.request.session['client_id'] = self.get_object().client.id
        self.request.session['back_to_curstat'] = self.request.path
        self.request.session['back_to_envcred'] = self.request.path

        context['back_to_apii'] = self.request.session['back_to_apii']
        context['table_curstatsummary'] = tables.CurrentStatusTable(
                    models.CurrentStatus.objects.filter(client=self.get_object().client))
        context['table_envcredsummary'] = tables.EnvironmentCredentialTable(
                    models.EnvironmentCredential.objects.filter(client=self.get_object().client))
        return context


class APIIntegrationDeleteView(generic.DeleteView):
    model = models.APIIntegrationSummary
    success_url = reverse_lazy('tracker:apitracksummary')


class CurrentStatusCreateView(generic.CreateView):
    model = models.CurrentStatus
    template_name = "tracker/curstatdetail.html"
    fields = ("client", "current_status", "current_status_details")
    

    def get_success_url(self):
        apii_id = self.request.session['apii_id']
        # print(">>>", apii_id)
        return reverse_lazy('tracker:apitrack_edit', kwargs={'pk':apii_id})

    def get_form(self):
        form = super().get_form()
        # print(">>>0", self.request.POST)
        initial_base = self.get_initial()
        
        client_id = self.request.session['client_id']
        initial_base['client'] = models.Client.objects.get(id=client_id)
       
        form.initial = initial_base

        form.fields['client'].disabled = True
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_to_curstat'] = self.request.session['back_to_curstat']

        return context


class CurrentStatusUpdateView(generic.UpdateView):
    model = models.CurrentStatus
    template_name = "tracker/curstatdetail.html"
    fields = ("client", "current_status", "current_status_details")

    def get_success_url(self):
        apii_id = self.request.session['apii_id']
        # print(">>>", apii_id)
        return reverse_lazy('tracker:apitrack_edit', kwargs={'pk':apii_id})

    def get_form(self):
        form = super().get_form()

        form.fields['client'].disabled = True
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_to_curstat'] = self.request.session['back_to_curstat']

        return context


class CurrentStatusDeleteView(generic.DeleteView):
    model = models.CurrentStatus
    
    def get_success_url(self):
        apii_id = self.request.session['apii_id']
        # print(">>>", apii_id)
        return reverse_lazy('tracker:apitrack_edit', kwargs={'pk':apii_id})


class EnvironmentCredentialCreateView(generic.CreateView):
    model = models.EnvironmentCredential
    template_name = "tracker/envcreddetail.html"
    fields = ("client", "key", "interfacelinks", "is_live", "eccompanyid", "customerid")
    

    def get_success_url(self):
        apii_id = self.request.session['apii_id']
        # print(">>>", apii_id)
        return reverse_lazy('tracker:apitrack_edit', kwargs={'pk':apii_id})

    def get_form(self):
        form = super().get_form()
        # print(">>>0", self.request.POST)
        initial_base = self.get_initial()
        
        client_id = self.request.session['client_id']
        initial_base['client'] = models.Client.objects.get(id=client_id)
       
        form.initial = initial_base

        form.fields['client'].disabled = True
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_to_envcred'] = self.request.session['back_to_envcred']

        return context


class EnvironmentCredentialUpdateView(generic.UpdateView):
    model = models.EnvironmentCredential
    template_name = "tracker/envcreddetail.html"
    fields = ("client", "key", "interfacelinks", "is_live", "eccompanyid", "customerid")

    def get_success_url(self):
        apii_id = self.request.session['apii_id']
        # print(">>>", apii_id)
        return reverse_lazy('tracker:apitrack_edit', kwargs={'pk':apii_id})

    def get_form(self):
        form = super().get_form()

        form.fields['client'].disabled = True
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_to_envcred'] = self.request.session['back_to_envcred']

        return context


class EnvironmentCredentialDeleteView(generic.DeleteView):
    model = models.EnvironmentCredential
    
    def get_success_url(self):
        apii_id = self.request.session['apii_id']
        # print(">>>", apii_id)
        return reverse_lazy('tracker:apitrack_edit', kwargs={'pk':apii_id})
