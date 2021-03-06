import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from . import models


class APIIntegrationSummaryTable(tables.Table):
    # edit = tables.LinkColumn('main:edit_item', args=[A('pk')], attrs={
    #     'a': {'class': 'btn'}
    # })
    edit = tables.LinkColumn('tracker:apitrack_edit', args=[A('pk')],
                            orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('tracker:apitrack_del', args=[A('pk')],
                            orderable=False, empty_values=(), verbose_name='')
    class Meta:
        model = models.APIIntegrationSummary
        attrs = {'class': 'table table-sm'}
        template_name = "django_tables2/bootstrap.html"
        fields = ("client", "last_active_discussion_date", "stage",
                  "important_notes", "answers_to_probing_questions",
                  "interface_shared", "environment_credentials",
                  "client_webhook_link", "client_webhook_sample",
                  "remarks")

    def render_edit(self):
        return 'Edit'

    def render_delete(self):
        return 'Delete'


class CurrentStatusTable(tables.Table):
    edit = tables.LinkColumn('tracker:curstat_edit', args=[A('pk')],
                            orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('tracker:curstat_del', args=[A('pk')],
                            orderable=False, empty_values=(), verbose_name='')

    class Meta:
        model = models.CurrentStatus
        attrs = {'class': 'table table-sm'}
        template_name = "django_tables2/bootstrap.html"
        fields = ("client", "entry_timestamp",
                  "current_status", "current_status_details")
    
    def render_edit(self):
        return 'Edit'

    def render_delete(self):
        return 'Delete'


class EnvironmentCredentialTable(tables.Table):
    edit = tables.LinkColumn('tracker:envcred_edit', args=[A('pk')],
                            orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('tracker:envcred_del', args=[A('pk')],
                            orderable=False, empty_values=(), verbose_name='')

    class Meta:
        model = models.EnvironmentCredential
        attrs = {'class': 'table table-sm'}
        template_name = "django_tables2/bootstrap.html"
        fields = ("client", "key", "interfacelinks", "is_live",
                  "eccompanyid", "customerid")

    def render_edit(self):
        return 'Edit'

    def render_delete(self):
        return 'Delete'

class ClientTable(tables.Table):

    class Meta:
        model = models.Client
        template_name = "django_tables2/bootstrap.html"
        fields = ("client_name", "client_company_name", "client_company_address", "is_live",
                  "client_company_phone", "gc_name1", "gc_name2")
