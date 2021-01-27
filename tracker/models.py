from django.db import models
from datetime import datetime


# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=200, unique=True, null=False)
    client_company_name = models.CharField(max_length=200, null=False)
    client_company_address = models.TextField(null=True)
    client_company_phone = models.CharField(max_length=200)
    gc_name1 = models.CharField(max_length=200, null=True)
    gc_name2 = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.client_name


class RefStage(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class RefInterface(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class APIIntegrationSummary(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT,
            related_name="client")
    last_active_discussion_date = models.DateTimeField()
    stage = models.ForeignKey(RefStage, on_delete=models.PROTECT)
    important_notes = models.TextField(null=True, blank=True)
    answers_to_probing_questions = models.TextField(null=True, blank=True)
    interface_shared = models.ForeignKey(RefInterface, on_delete=models.PROTECT)
    environment_credentials = models.TextField(null=True, blank=True)
    client_webhook_link = models.TextField(null=True, blank=True)
    client_webhook_sample = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    waybill_format_notes = models.TextField(null=True, blank=True)


class CurrentStatus(models.Model):
    client = models.ForeignKey(Client,
        on_delete=models.CASCADE)
    entry_timestamp = models.DateTimeField(default=datetime.now())
    current_status = models.CharField(max_length=500)
    current_status_details = models.TextField(null=True)

    def __str__(self):
        return self.current_status

class EnvironmentCredential(models.Model):
    client = models.ForeignKey(Client,
        on_delete=models.CASCADE)
    key = models.CharField(max_length=200, unique=True, null=False)
    interfacelinks = models.TextField(null=True)
    is_live = models.BooleanField(default=False)
    eccompanyid = models.CharField(max_length=200)
    customerid = models.CharField(max_length=200)

    def __str__(self):
        return self.eccompanyid
