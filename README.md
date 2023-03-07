#MeshZen
MeshZen is a web-based platform that allows users to access and visualize 3D spine meshes from the Zenodo repository. It is built on top of Django and Django Rest Framework, and provides powerful search and visualization tools for spine researchers.

#Installation
Clone the repository to your local machine.
Install the required packages using pip install -r requirements.txt.
Set up the database by running python manage.py migrate.
Create a superuser account by running python manage.py createsuperuser.
Start the development server with python manage.py runserver.

#Usage
MeshZen provides a web-based interface for users to search and visualize 3D spine meshes. Users can create an account, search for meshes based on various criteria such as metadata or mesh type, and visualize meshes using advanced tools such as lighting, shading, and camera control. Meshes can also be exported to popular formats such as OBJ, STL, and PLY for use in other software and analysis tools.

#API
MeshZen also provides a REST API for programmatic access to the platform. The API allows users to search for meshes, retrieve metadata, and download meshes in various formats. The API is documented using Swagger, and can be accessed at /api/docs.

#Contributing
Contributions to MeshZen are welcome and encouraged! To contribute, please fork the repository and submit a pull request with your changes. Please also ensure that your code passes all tests and adheres to the project's code style guidelines.

#License
MeshZen is released under the MIT License. See LICENSE for more information.