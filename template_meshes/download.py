import requests

# URL of the API endpoint
url = "http://lifesciencedb.jp/bp3d/API/image"

# Parameters for the API request
params = {
    "Common": {
        "Version": "4.1",
        "TreeName": "partof"
    },
    "Part": [
        {
            "PartID": "FMA64964",
            "PartColor": "FFB8C6",
            "PartOpacity": 0.5
        }
    ],
    "Mesh": [
        {
            "MeshName": "cervical spine",
            "MeshFormat": "stl"
        }
    ]
}

# Send the API request
response = requests.get(url, params=params)

# Save the .stl file
with open("cervical_spine.stl", "wb") as f:
    f.write(response.content)
