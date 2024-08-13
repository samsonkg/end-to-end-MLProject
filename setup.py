from setuptools import find_packages, setup

from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requiremnts
    '''
    requirements=[]
    with open(file_path) as file_obj: # file_obj is a temporary 
        requirements=file_obj.readlines()
        # the above reads the libraries/... in the requirements.txt file line by line but also reads the new line, \n. thus, to avoid this, add the ff line of code
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
setup(
    name="mlproject",
    version="0.0.1",
    author="Samson",
    author_email="samsoneea@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)