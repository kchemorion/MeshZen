import pyvista as pv

# Load the .stl file
mesh = pv.read('Vertebra.stl')

# Triangulate the mesh to create a vtkUnstructuredGrid object
ugrid = mesh.triangulate()

# Write the unstructured grid to a .glTF file
pv.save_glb(ugrid, 'Vertebra.glb')
