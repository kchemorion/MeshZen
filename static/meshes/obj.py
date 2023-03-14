import os
import sys
import vtk

# Define function to recursively find OBJ files in a folder
def find_obj_files(folder):
    obj_files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.obj'):
                obj_files.append(os.path.join(dirpath, filename))
    return obj_files

# Create folder for VTK files
vtk_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "vtk_files")
if not os.path.exists(vtk_folder):
    os.makedirs(vtk_folder)

# Convert OBJ files to VTK
obj_files = find_obj_files(os.getcwd())
num_files = len(obj_files)
for i, obj_file in enumerate(obj_files):
    reader = vtk.vtkOBJReader()
    reader.SetFileName(obj_file)
    reader.Update()

    vtk_file = os.path.join(vtk_folder, os.path.splitext(os.path.basename(obj_file))[0] + ".vtk")
    writer = vtk.vtkDataSetWriter()
    writer.SetInputData(reader.GetOutput())
    writer.SetFileName(vtk_file)
    writer.Write()

    # Display progress
    progress = (i+1)/num_files*100
    sys.stdout.write("\rConverting files: %d%%" % progress)
    sys.stdout.flush()

print("\nConversion complete.")
