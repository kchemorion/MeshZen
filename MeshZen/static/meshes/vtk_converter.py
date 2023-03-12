import os
import sys
import vtk

# Define function to recursively find STL files in a folder
def find_stl_files(folder):
    stl_files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.stl'):
                stl_files.append(os.path.join(dirpath, filename))
    return stl_files

# Create folder for VTK files
vtk_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "vtk_files")
if not os.path.exists(vtk_folder):
    os.makedirs(vtk_folder)

# Convert STL files to VTK
stl_files = find_stl_files(os.getcwd())
num_files = len(stl_files)
for i, stl_file in enumerate(stl_files):
    reader = vtk.vtkSTLReader()
    reader.SetFileName(stl_file)
    reader.Update()

    vtk_file = os.path.join(vtk_folder, os.path.splitext(os.path.basename(stl_file))[0] + ".vtk")
    writer = vtk.vtkDataSetWriter()
    writer.SetInputData(reader.GetOutput())
    writer.SetFileName(vtk_file)
    writer.Write()

    # Display progress
    progress = (i+1)/num_files*100
    sys.stdout.write("\rConverting files: %d%%" % progress)
    sys.stdout.flush()

print("\nConversion complete.")
