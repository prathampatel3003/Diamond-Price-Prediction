from setuptools import setup, find_packages,setup
from typing import List

Hypen_E_dot = '-e .'

def get_reqirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if Hypen_E_dot in requirements:
            requirements.remove(Hypen_E_dot)
        
        return requirements

setup(
    name="diamondpricepredition",  
    version="0.0.1",  
    author="pratham",
    author_email="ppratham3003@.com",
    install_requries=get_reqirements("requirements.txt"),
    packages=find_packages(),

    
)
