from dataclasses import field
import imp
from pyexpat import model
from django.forms import ModelForm
from .models import Projects


class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'description',
                  'demmo_link', 'source_link', 'tags', 'featured_image']
