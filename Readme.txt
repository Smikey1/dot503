Build Automation for Calculator Application
This document provides instructions on how to use the build automation script for the Calculator application.

Requirements
- Python 3.x
- Git
- pip (Python package installer)

Pre Setup
By following Pre-Setup, It skip all the Instructions steps.
You can directly download the build.py file from below link: https://github.com/Smikey1/dot503/blob/master/build.py

Once downloaded, you can run the below python command and it will do everything for you.
python build.py run 

Once the application is up/running, you can open your browser and visit:
http://127.0.0.1:5000.

Or Visit the live deployed application using the link:
https://dot503.onrender.com

Instructions
1. Clone the repository:
If you haven't cloned the repository yet, you can do so by running:
git clone https://github.com/Smikey1/dot503.git

2. Navigate to the project directory:
Navigate into the project directory after cloning it:
cd dot503

3. Run the build script:
You can run the build script with the following command:
python build.py <target>
Allowed Targets:
* run: Clones the repository from GitHub, installs required dependencies, packages the application, and runs it.
* clean: Performs final cleanup of files and directories.
Example:
python build.py run 
python build.py clean

This will perform the following actions:
* Clone the repository
* Create a virtual environment
* Install dependencies
* Run tests
* Package the application
* Run the application

Once the application is up/running, you can open your browser and visit: http://127.0.0.1:5000.
Or Visit the live deployed application using the link: https://dot503.onrender.com

4. Clean up:
To remove all the build artifacts, virtual environments, and other temporary files, run the clean target:
python build.py clean

This will clean up the repository by removing all generated files and directories that are no longer needed.
