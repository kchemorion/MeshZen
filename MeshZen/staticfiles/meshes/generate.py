import openai
import random

openai.api_key = "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"

import openai
import random

openai.api_key = "YOUR_API_KEY"

def generate_mesh_string():
    mesh_string = "solid hypothetical_spine\n"
    for i in range(12):
        facet_normal = [round(random.uniform(-1, 1), 5) for _ in range(3)]
        vertex_1 = [round(random.uniform(-1, 1), 5) for _ in range(3)]
        vertex_2 = [round(random.uniform(-1, 1), 5) for _ in range(3)]
        vertex_3 = [round(random.uniform(-1, 1), 5) for _ in range(3)]
        mesh_string += "facet normal {} {} {}\n".format(*facet_normal)
        mesh_string += "outer loop\n"
        mesh_string += "vertex {} {} {}\n".format(*vertex_1)
        mesh_string += "vertex {} {} {}\n".format(*vertex_2)
        mesh_string += "vertex {} {} {}\n".format(*vertex_3)
        mesh_string += "endloop\n"
        mesh_string += "endfacet\n"
    mesh_string += "property SpinopelvicParameter PI {}\n".format(round(random.uniform(3, 4), 5))
    mesh_string += "property SpinopelvicParameter PT {}\n".format(round(random.uniform(2, 3), 5))
    mesh_string += "property SpinopelvicParameter SS {}\n".format(round(random.uniform(1.5, 2), 5))
    mesh_string += "property SpinopelvicParameter LL {}\n".format(round(random.uniform(1, 1.5), 5))
    mesh_string += "property SpinopelvicParameter LL-PI {}\n".format(round(random.uniform(0.5, 1), 5))
    mesh_string += "property SpinopelvicParameter GT {}\n".format(round(random.uniform(0.5, 1), 5))
    mesh_string += "property SpinopelvicParameter RPV {}\n".format(round(random.uniform(1.5, 2), 5))
    mesh_string += "property SpinopelvicParameter RLL {}\n".format(round(random.uniform(1, 1.5), 5))
    mesh_string += "property SpinopelvicParameter LDI {}\n".format(round(random.uniform(0.5, 1), 5))
    mesh_string += "property SpinopelvicParameter RSA {}\n".format(round(random.uniform(0.2, 0.5), 5))
    mesh_string += "property SpinopelvicParameter TPA {}\n".format(round(random.uniform(0.5, 1), 5))
    mesh_string += "endsolid hypothetical_spine\n"
    return mesh_string

for i in range(1000):
    mesh_string = generate_mesh_string()
    file_name = "hypothetical_spine_{}.stl".format(i)
    with open(file_name, "w") as f:
        f.write(mesh_string)
    print("File saved: {}".format(file_name))
