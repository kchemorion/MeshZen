from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib import messages

from .forms import MeshSearchForm
from .models import ZenodoDeposition
from django.conf import settings

import requests
import json
from datetime import datetime, timezone
from dateutil.parser import parse as parse_date

class MeshSearchView(ListView):
    model = ZenodoDeposition
    template_name = 'meshes/mesh_search_results.html'
    context_object_name = 'mesh_depositions'
    paginate_by = settings.PAGINATION_SIZE

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            depositions = ZenodoDeposition.objects.filter(title__icontains=q)
            if not depositions.exists():
                # perform a Zenodo search and cache the results
                search_url = f'https://zenodo.org/api/records/?size=100&q={q}+AND+spine+AND+type:dataset'
                response = requests.get(search_url)
                if response.status_code == 200:
                    response_data = json.loads(response.text)
                    for record in response_data['hits']['hits']:
                        deposition = ZenodoDeposition.objects.create(
                            title=record['metadata']['title'],
                            deposition_id=record['id'],
                            description=record['metadata'].get('description', ''),
                            keywords=','.join(record['metadata'].get('keywords', [])),
                            created_date=parse_date(record['created']),
                            published_date=parse_date(record['metadata'].get('publication_date', '')),
                        )
                        # add mesh files
                        for file in record['files']:
                            if file['type'] == 'mesh':
                                mesh_file = MeshFile.objects.create(
                                    filename=file['key'],
                                    size=file['size'],
                                    download_url=file['links']['download'],
                                    deposition=deposition
                                )
                    # return the queryset
                    depositions = ZenodoDeposition.objects.filter(title__icontains=q)
                    if not depositions.exists():
                        messages.error(self.request, f"No results found for '{q}'")
            return depositions
        return ZenodoDeposition.objects.none()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MeshSearchForm(self.request.GET)
        return context
