# Django imports
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View

# Netbox imports
from netbox.views import generic

# Internal imports
from . import forms, models, tables

class HomeView(View):
    """Homepage"""
    template_name = 'netbox_zabbix/home.html'

    # service incoming GET HTTP requests
    def get(self, request):
        """Get request."""
        return render(
            request,
            self.template_name,
            {
                "github": github.repositories,
            }
        )