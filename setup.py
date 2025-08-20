from setuptools import setup,find_packages
from typing import List

def find_requirements(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n'," ") for  req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
        return requirements


setup(
    name="ml_project_1",
    version="0.1.0",
    author="vamsi",
    author_email="vamsigandavarapu101@gmail.com",
    packages=find_packages(),
    install_requires=find_requirements("requirements.txt")
    
    
    
    
    
    
    
    
)