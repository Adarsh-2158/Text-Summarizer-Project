import os
from pathlib import Path   #
import logging #i want to log all info during real time

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", #__init__.py (constructor file) is used to mark a directory as a Python package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile", #docker image of the source code and deployment in EC2 machine in AWS
    "requirements.txt",
    "setup.py", #to install the package
    "research/trials.ipynb", #jupyter notebook for trials 
]
#to do local imports we need above folders

for filepath in list_of_files:
    #handling paths like backward slash or forward slash there is a library that i included called "Pathlib"
    filepath = Path(filepath) #converting to path object
    filedir, filename = os.path.split(filepath) #splitting the path into directory and filename
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) #creating directories if they do not exist
        logging.info(f"Creating directory: {filedir} for file: {filename}") #just for records in the log file

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #if file does not exist or it is empty 
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}") #just for records in the log file
    
    else:
        logging.info(f"{filename} is already exists ")