from django.db.models import Q
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from .models import ZenodoDeposition, MeshFile
import os
import base64
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render

def results(request):
    # retrieve data from database or other source
    data = {
        'results': [
            {'field1': 'value1', 'field2': 'value2', 'field3': 'value3'},
            {'field1': 'value4', 'field2': 'value5', 'field3': 'value6'},
        ]
    }
    return render(request, 'meshes/results.html', context=data)


def analyze(request):

    return render(request, 'meshes/fea.html')

def report(request):

    return render(request, 'meshes/report.html')


@method_decorator(csrf_exempt, name='dispatch')
class MeshSearchView(ListView):
    template_name = 'meshes/mesh_search_results.html'
    context_object_name = 'mesh_files'
    paginate_by = settings.PAGINATION_SIZE
    model = MeshFile
    
    def get_queryset(self):
        q = self.request.GET.get('q')
        pi = self.request.GET.get('pi')
        pt = self.request.GET.get('pt')
        ss = self.request.GET.get('ss')
        ll = self.request.GET.get('ll')
        if q or pi or pt or ss or ll :
            mesh_files = MeshFile.objects.all()
            if q:
                mesh_files = mesh_files.filter(Q(filename__icontains=q) | Q(deposition__title__icontains=q))
            if pi:
                mesh_files = mesh_files.filter(pi=pi)
            if pt:
                mesh_files = mesh_files.filter(pt=pt)
            if ss:
                mesh_files = mesh_files.filter(ss=ss)
            if ll:
                mesh_files = mesh_files.filter(ll=ll)
            return mesh_files
        return MeshFile.objects.none()

def visualize(request):
    context = {
        'STATIC_URL': settings.STATIC_URL,
    }
    return render(request, 'meshes/oops.html', context=context)

