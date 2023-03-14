import vtk

# Read the STL file
reader = vtk.vtkSTLReader()
reader.SetFileName("Vertebra.stl")
reader.Update()

# Write the OBJ file
writer = vtk.vtkOBJWriter()
writer.SetInputData(reader.GetOutput())
writer.SetFileName("Vertebra.obj")
writer.Write()
