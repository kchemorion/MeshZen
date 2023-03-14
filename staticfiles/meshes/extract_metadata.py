import os
import sqlite3
import re

# Connect to the database
conn = sqlite3.connect('db.sqlite3')

# Create a cursor
c = conn.cursor()

# Create the mesh_values table
c.execute('''CREATE TABLE IF NOT EXISTS mesh_values
             (filename text, pi integer, pt integer, ss integer, ll integer)''')

# Define a function to extract the parameters from a file name
def extract_parameters(filename):
    # Use regular expressions to extract the parameters from the file name
    match = re.match(r'^mesh_(?P<pi>-?\d+)_(?P<pt>-?\d+)_(?P<ss>-?\d+)_(?P<ll>-?\d+).ply$', filename)
    if match:
        pi = int(match.group('pi'))
        pt = int(match.group('pt'))
        ss = int(match.group('ss'))
        ll = int(match.group('ll'))
        return (pi, pt, ss, ll)
    else:
        return None

# Recursively iterate over the meshes directory
for root, dirs, files in os.walk('.'):
    for file in files:
        # Check if the file is a STL file
        if file.endswith('.stl'):
            # Extract the parameters from the file name
            parameters = extract_parameters(file)
            if parameters:
                # Insert the parameters into the mesh_values table
                filename = os.path.join(root, file)
                c.execute("INSERT INTO mesh_values (filename, pi, pt, ss, ll) VALUES (?, ?, ?, ?, ?)",
                          (filename,) + parameters)

# Commit the changes and close the connection
conn.commit()
conn.close()
