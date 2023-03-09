from django.shortcuts import render

import os
import vtk
from django.shortcuts import render
from django.conf import settings

def home(request):
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

    return render(request, 'base/landing.html')


def about(request):
    return render(request, 'base/about.html')

def documentation(request):
    return render(request, 'base/documentation.html')

def contact(request):
    return render(request, 'base/contact.html')

def features(request):
    return render(request, 'base/features.html')

def download(request):
    return render(request, 'base/download.html')