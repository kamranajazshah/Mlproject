from setuptools import  find_packages,setup
from typing import List
HYPHEN_DOT= '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    this function gather requirements 
    """
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)
    return requirements

setup(
    name="DATA SCIENCE PROJECT",
    version="0.0.1",
    author= "kamran",
    author_email="kamranajazshah@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements("requirements.txt")
)
