from django.db.models import Q
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from .models import ZenodoDeposition, MeshFile
import os
import vtk

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

def visualize(request):
    # Get the path to the mesh file
    mesh_file = os.path.join(settings.STATIC_ROOT, 'meshes', 'Vertebra.stl')

    # Read the mesh file
    reader = vtk.vtkSTLReader()
    reader.SetFileName(mesh_file)
    reader.Update()

    # Create a mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(1, 0, 0)  # set the color of the actor

    # Create a renderer, render window, and interactor
    renderer = vtk.vtkRenderer()
    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)

    # Add the actor to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(0.2, 0.2, 0.2)  # set the background color of the scene

    # Render the scene and start the interactor
    render_window.Render()
    interactor.Start()

    return render(request, 'meshes/results.html')

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

