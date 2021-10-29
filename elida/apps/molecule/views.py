from django.views.generic import ListView, DetailView

from .models import Molecule


class MoleculeListView(ListView):
    model = Molecule
    template_name = 'molecule_list.html'
    extra_context = {'title': 'Molecules', 'datatable_class': 'molecule-table', 'table_heading': 'Molecules'}
