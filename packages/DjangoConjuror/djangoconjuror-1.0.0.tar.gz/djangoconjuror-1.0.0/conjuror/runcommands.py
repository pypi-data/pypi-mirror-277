import subprocess
import shutil
import sys
import os

def create_django_project(path, project_name):
    try:
        os.chdir(path)
        subprocess.run(["python", "-m", "django", "startproject", project_name], check=True)
        #create_constants(path, project_name)
        print(f"Django project '{project_name}' created successfully in {path}")
    except subprocess.CalledProcessError:
        print(f"Failed to create Django project. Make sure Django is installed and the path is correct.")
    except Exception as e:
        print(f"Error creating Django project: {e}")

def create_constants(path,project_name):
    constants_filename = os.path.join(path,project_name)
    constants_filename = os.path.join(constants_filename,"constants.py")
    constant_name = "SERVER_IP"
    constant_value = "127.0.0.1"
    with open(constants_filename, 'w') as file:
        file.write(f"{constant_name} = '{constant_value}'\n")
    if path is None:
        path = find_manage_py_path(os.getcwd(),project_name)
        if path is None:
            print("No Django project found. Please specify a project path or run this command inside a Django project directory.")
            return
    directory_name = os.path.basename(path)
    settings_file_path = os.path.join(path, directory_name, 'settings.py')
    if not os.path.exists(settings_file_path):
        print("Settings file not found. Please make sure it exists in the main app directory.")
        sys.exit(1)

    with open(settings_file_path, 'r') as f:
        lines = f.readlines()

    import_os_line_index = None
    for i, line in enumerate(lines):
        if 'from pathlib import Path' in line:
            import_os_line_index = i
        if 'ALLOWED_HOSTS = []' in line:
            lines[i] = 'ALLOWED_HOSTS = [SERVER_IP]\n'  # Direct replacement of the line

    if import_os_line_index is not None and 'from constants import *' not in lines:
        lines.insert(import_os_line_index + 1, "from constants import *\n")

    with open(settings_file_path, 'w') as f:
        f.write("".join(lines))

    
def create_django_apps(app_names,project_name=None, path=None):
    if path is None:
        path = find_manage_py_path(os.getcwd(),project_name)
        if path is None:
            print("No Django project found. Please specify a project path or run this command inside a Django project directory.")
            return

    try:
        project_path = os.path.join(path)
        os.chdir(project_path)
        for app_name in app_names:
            apps = app_name.split(',')
            for app in apps:
                subprocess.run(["python", "manage.py", "startapp", app], check=True)
                update_settings_file_apps(project_path,app)
                print(f"Django app '{app}' created successfully in {project_path}")
    except subprocess.CalledProcessError:
        print("Failed to create Django app. Make sure you are inside a Django project directory and Django is installed.")
    except Exception as e:
        print(f"Error creating Django app: {e}")

def update_settings_file_apps(project_path,app):
    directory_name = os.path.basename(project_path)
    settings_file_path = os.path.join(project_path, directory_name, 'settings.py')
    if not os.path.exists(settings_file_path):
        print("Settings file not found. Please make sure it exists in the main app directory.")
        sys.exit(1)

    with open(settings_file_path, 'r') as f:
        lines = f.readlines()
    apps_line_index = None
    for i, line in enumerate(lines):
        if 'INSTALLED_APPS = ' in line.strip():
            apps_line_index = i + 1 
        
    if apps_line_index is not None:
        if apps_line_index is not None:
            lines.insert(apps_line_index, f"'{app}',\n")

    with open(settings_file_path, 'w') as f:
        f.write("".join(lines))

def create_static_and_templates_folders(project_path):
    static_path = os.path.join(project_path, 'static')
    templates_path = os.path.join(project_path, 'templates')

    os.makedirs(static_path, exist_ok=True)
    os.makedirs(templates_path, exist_ok=True)

def update_settings_file(project_path):
    directory_name = os.path.basename(project_path)
    settings_file_path = os.path.join(project_path, directory_name, 'settings.py')
    if not os.path.exists(settings_file_path):
        print("Settings file not found. Please make sure it exists in the main app directory.")
        sys.exit(1)

    with open(settings_file_path, 'r') as f:
        lines = f.readlines()

    static_line_index = None
    templates_line_index = None
    import_os_line_index = None
    for i, line in enumerate(lines):
        if 'from pathlib import Path' in line:
            import_os_line_index = i
        if 'STATIC_URL' in line:
            static_line_index = i
        if 'TEMPLATES = ' in line.strip():
            templates_line_index = i + 1 

    if import_os_line_index is not None and 'import os' not in lines:
        lines.insert(import_os_line_index + 1, "import os\n")

    if static_line_index is not None:
        lines.insert(static_line_index + 2, 'STATICFILES_DIRS = [BASE_DIR, "static"]\n')

    if templates_line_index is not None:
        while 'DIRS' not in lines[templates_line_index]:
            templates_line_index += 1 
        lines[templates_line_index] = lines[templates_line_index].replace(
            "'DIRS': []",
            "'DIRS': [BASE_DIR, 'templates']",
        )
    

    with open(settings_file_path, 'w') as f:
        f.write("".join(lines))


def find_manage_py_path(start_path, project_name=None):
    for root, dirs, files in os.walk(start_path):
        if 'manage.py' in files:
            if project_name:
                folder_name = os.path.basename(root)
                if folder_name == project_name:
                    return root
            else:
                return root
    return None
