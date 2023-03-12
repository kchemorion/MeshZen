import vtk

# Read the STL file
reader = vtk.vtkSTLReader()
reader.SetFileName("Vertebra.stl")
reader.Update()

# Write the VTK file
writer = vtk.vtkDataSetWriter()
writer.SetInputData(reader.GetOutput())
writer.SetFileName("Vertebra.vtk")
writer.Write()
