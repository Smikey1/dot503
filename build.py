import os
import subprocess
import tarfile
import shutil

# Variables
REPO_URL = "https://github.com/Smikey1/dot503.git"  # URL of the repository to clone
CLONE_DIR = "dot503"                                # Directory where the repo will be cloned
APP_NAME = "my_flask_app"                           # Change this to your Flask app name
VENV_DIR = "venv"                                   # Virtual environment directory
REQUIREMENTS = "requirements.txt"
PORT = 5000                                         # Port for running the Flask app

def clone():
    # Remove the existing directory if it exists
    if os.path.exists(CLONE_DIR):
        print(f"Removing existing directory {CLONE_DIR}...")
        shutil.rmtree(CLONE_DIR)

    print("Cloning the repository...")
    subprocess.run(["git", "clone", REPO_URL, CLONE_DIR], check=True)

def create_virtualenv():
    if not os.path.exists(VENV_DIR):
        print(f"Creating virtual environment in {VENV_DIR}...")
        subprocess.run(["python", "-m", "venv", VENV_DIR], check=True)

    # Directly use the virtual environment's python executable
    python_path = os.path.join(VENV_DIR, "Scripts", "python") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")
    print(f"Using Python from virtual environment: {python_path}")
    subprocess.run([python_path, "-m", "ensurepip", "--upgrade"], check=True)
    subprocess.run([python_path, "-m", "pip", "install", "--upgrade", "pip"], check=True)


def install_dependencies():
    print("Installing dependencies...")
    pip_path = os.path.join(VENV_DIR, "Scripts", "pip") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "pip")
    subprocess.run([pip_path, "install", "-r", os.path.join(CLONE_DIR, REQUIREMENTS)], check=True)

def verify_dependencies():
    python_path = os.path.join(VENV_DIR, "Scripts", "python") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")
    subprocess.run([python_path, "-m", "pip", "show", "waitress"], check=True)

def run_tests():
    print("Running tests...")
    # Adjust sys.path to include the cloned directory
    sys.path.insert(0, CLONE_DIR)  # Add 'dot503' to the Python path
    python_path = os.path.join(VENV_DIR, "Scripts", "python") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")
    test_file = os.path.join(CLONE_DIR, "build_test_operations.py")
    subprocess.run([python_path, "-m", "unittest", test_file])

def package_application():
    print("Packaging the application...")
    with tarfile.open(f"{APP_NAME}.tar.gz", "w:gz") as tar:
        tar.add(CLONE_DIR, arcname=os.path.basename(CLONE_DIR))

def run_development_server_application():
    print("Running the application...")
    # Determine the python path based on the operating system
    python_path = os.path.join(VENV_DIR, "Scripts", "python") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")
    app_path = os.path.join(CLONE_DIR, "app.py")
    subprocess.run([python_path, app_path], check=True)

def run_production_server_application():
    print("Running the application with Waitress...")
    print("Running on http://127.0.0.1:5000")

    # For Windows, use Waitress instead of Gunicorn
    python_path = os.path.join(VENV_DIR, "Scripts", "python") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")
    subprocess.run([python_path, "-m", "waitress", "serve", "app:app"], check=True)


def clean():
    print("Cleaning up...")
    # For Windows compatibility, we will use shutil to remove files
    shutil.rmtree(VENV_DIR, ignore_errors=True)
    subprocess.run(["rm", "-rf", CLONE_DIR], check=True, shell=True)
    if os.path.exists(f"{APP_NAME}.tar.gz"):
        os.remove(f"{APP_NAME}.tar.gz")

def main(target):
    if target == "run":
        print("Creating and Activating the virtual environment...")
        clone()
        create_virtualenv()
        install_dependencies()
        verify_dependencies()
        run_tests()
        package_application()
        run_production_server_application()
    elif target == "clean":
        clean()
    else:
        print("Invalid target specified.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("\033[1;33mUsage: python build.py <target>\033[0m\n")  # Bold Yellow for 'Usage'
        print("\033[1;32mAllowed Targets:\033[0m")  # Bold Green for 'Allowed Targets'
        print("\033[1;36m  1) run:\033[0m \033[3mClones the repository from GitHub, installs required dependencies, packages the application, and runs it.\033[0m")
        print("\033[1;36m  2) clean:\033[0m \033[3mPerforms final cleanup of files and directories.\033[0m\n")
        print("\033[1;37mExample:\033[0m")
        print("  \033[1;30mpython build.py run\033[0m")  
        print("  \033[1;30mpython build.py clean\033[0m\n") 
    else:
        main(sys.argv[1])

