import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
INSTALLED_APPS = ['collaboration', 'documentation', 'meshes', 'users', 'visualizations']

for app in INSTALLED_APPS:
    app_path = os.path.join(PROJECT_PATH, app)
    urls_path = os.path.join(app_path, 'urls.py')
    if not os.path.exists(urls_path):
        with open(urls_path, 'w') as urls_file:
            urls_file.write('from django.urls import path\n\n')
            urls_file.write('urlpatterns = [\n')
            urls_file.write('    # Add your URL patterns here\n')
            urls_file.write(']\n')
