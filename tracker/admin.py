from django.contrib import admin
from .models import (RefStage, Client, RefInterface, CurrentStatus,
                     EnvironmentCredential)

# Register your models here.
admin.site.register(RefStage)
admin.site.register(Client)
admin.site.register(RefInterface)
admin.site.register(CurrentStatus)
admin.site.register(EnvironmentCredential)
