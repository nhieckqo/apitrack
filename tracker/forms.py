from django import forms
from . import models


class APIIntegrationForm(forms.ModelForm):
    # important_notes = forms.CharField(widget=forms.Textarea,blank=True)
    # answers_to_probing_questions = forms.CharField(widget=forms.Textarea,blank=True)
    # environment_credentials = forms.CharField(widget=forms.Textarea,blank=True)
    # client_webhook_link = forms.CharField(widget=forms.Textarea,blank=True)
    # client_webhook_sample = forms.CharField(widget=forms.Textarea,blank=True)
    # remarks = forms.CharField(widget=forms.Textarea,blank=True)
    # waybill_format_notes = forms.CharField(widget=forms.Textarea,blank=True)

    class Meta:
        model = models.APIIntegrationSummary
        fields = ('client', 'last_active_discussion_date', 'stage',
                  'important_notes', 'answers_to_probing_questions',
                  'interface_shared', 'environment_credentials',
                  'client_webhook_link', 'client_webhook_sample',
                  'remarks', 'waybill_format_notes')
