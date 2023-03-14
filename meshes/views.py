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
import pymeshlab as ml

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
    # Load the mesh using pymeshlab
    mesh_path = os.path.join(settings.STATICFILES_DIRS[0], 'meshes/Vertebra.stl')
    ms = ml.MeshSet()
    ms.load_new_mesh(mesh_path)
    mesh = ms.current_mesh()

    # Simplify the mesh using pymeshlab
    ms2 = ml.MeshSet()
    ms2.add_mesh(mesh)
    ms2.apply_filter('simplification_quadric_edge_collapse_decimation', targetfacenum=1000)
    simplified_mesh = ms2.current_mesh()

    # Write the mesh to an STL file
    stl_path = os.path.join(settings.MEDIA_ROOT, 'meshes/simplified_mesh.stl')
    ms2.save_current_mesh(stl_path)

    # Read the contents of the STL file as a binary string
    with open(stl_path, 'rb') as f:
        stl_contents = f.read()
    base64_stl = base64.b64encode(stl_contents).decode('utf-8')

    # Generate context data for the template
    context = {
        'STATIC_URL': settings.STATIC_URL,
        'mesh_url': 'data:application/stl;base64,' + base64_stl
    }
    return render(request, 'meshes/oops.html', context=context)


